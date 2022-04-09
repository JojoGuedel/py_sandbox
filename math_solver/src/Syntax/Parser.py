from Diagnostics.DiagnosticBag import DiagnosticBag
from Diagnostics.Kind.UnexpectedToken import UnexpectedToken
from Syntax.Node.Invalid import Invalid
from Syntax.Node.BinaryExpression import BinaryExpression
from Syntax.Node.Equation import Equation
from Syntax.Node.Function import Function
from Syntax.Node.Literal import Literal
from Syntax.Node.Number import Number
from Syntax.Node.ParenthesizedExpression import ParenthesizedExpression
from Syntax.Node.SyntaxNode import SyntaxNode
from Syntax.Node.Token import Token
from Syntax.Node.UnaryExpression import UnaryExpression
from Syntax.TokenKind import TokenKind


class Parser:
    def __init__(self, tokens: list[Token], diagnostics: DiagnosticBag):
        self._pos: int = 0
        self._tokens: list[Token] = tokens
        self._valid_token = self._current_token().kind != TokenKind.Invalid
        self._diagnostics: DiagnosticBag = diagnostics
        self.tree: SyntaxNode

    def _current_token(self):
        if self._pos >= 0 and self._pos < len(self._tokens):
            return self._tokens[self._pos]

        else:
            return Token(TokenKind.Invalid, self._pos, 0)

    def _advance(self):
        token = self._current_token()
        self._pos += 1
        self._valid_token = self._current_token().kind != TokenKind.Invalid
        return token

    def _expect_kind(self, *token_kinds: TokenKind):
        if len(token_kinds) < 1:
            raise

        current_token = self._current_token()

        for token_kind in token_kinds:
            if current_token.kind == token_kind:
                return self._advance()

        if self._valid_token:
            self._diagnostics.append(UnexpectedToken(self._current_token(), token_kinds[0]))
        return Token(token_kinds[0], self._current_token().pos, self._current_token().length)

    def parse(self):
        self.tree = self._parse_expression()
        self._expect_kind(TokenKind.End)

    def _parse_expression(self):
        return self._parse_equation()

    def _parse_equation(self):
        left = self._parse_binary_expression()

        if self._current_token().kind == TokenKind.Equal:
            operator = self._advance()
            right = self._parse_expression()

            return Equation(left, operator, right)

        return left

    def _parse_binary_expression(self, operator_precedence = Token.MAX_PRECEDENCE):
        if operator_precedence == 0:
            return self._parse_unary_expression()

        left = self._parse_binary_expression(operator_precedence - 1)

        while self._current_token().precedence() == operator_precedence:
            operator = Token(TokenKind.Star, self._current_token().pos, 0) if operator_precedence == Token.IMPLICIT_MULT_PRECEDENCE else self._advance()
            right = self._parse_binary_expression(operator_precedence - 1)
            left = BinaryExpression(left, operator, right)

        return left

    def _parse_unary_expression(self):
        if self._current_token().kind == TokenKind.Plus or self._current_token().kind == TokenKind.Minus:
            operator = self._advance()
            right = self._parse_unary_expression()

            return UnaryExpression(operator, right)

        return self._parse_primary()

    def _parse_primary(self):
        current_token = self._current_token()

        if current_token.kind == TokenKind.FunctionName:
            return self._parse_function()

        elif (current_token.kind == TokenKind.LParen):
            l_paren = self._advance()
            expr = self._parse_expression()
            r_paren = self._expect_kind(TokenKind.RParen)

            return ParenthesizedExpression(l_paren, expr, r_paren)

        elif current_token.kind == TokenKind.Number:
            return Number(self._advance())

        elif current_token.kind == TokenKind.Literal:
            return Literal(self._advance())

        else:
            if self._valid_token:
                self._diagnostics.append(UnexpectedToken(self._current_token()))
            return Invalid(self._advance())

    def _parse_function(self):
        function_name = self._advance()
        l_paren = self._expect_kind(TokenKind.LParen)

        args: list[SyntaxNode] = []
        if self._current_token().kind != TokenKind.RParen:
            args.append(self._parse_expression())

            while self._current_token().kind == TokenKind.Comma:
                self._pos += 1
                args.append(self._parse_expression())

        r_paren = self._expect_kind(TokenKind.RParen)

        return Function(function_name, l_paren, args, r_paren)
