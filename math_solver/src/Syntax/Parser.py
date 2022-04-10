from Diagnostics.DiagnosticBag import DiagnosticBag
from Diagnostics.Kind.UnexpectedToken import UnexpectedToken
from Syntax.Node.InvalidSyntax import InvalidSyntax
from Syntax.Node.BinaryExpressionSyntax import BinaryExpressionSyntax
from Syntax.Node.EquationSyntax import EquationSyntax
from Syntax.Node.FunctionSyntax import FunctionSyntax
from Syntax.Node.LiteralSyntax import LiteralSyntax
from Syntax.Node.NumberSyntax import NumberSyntax
from Syntax.Node.ParenthesizedExpressionSyntax import ParenthesizedExpressionSyntax
from Syntax.Node.SyntaxNode import SyntaxNode
from Syntax.Node.SyntaxToken import SyntaxToken
from Syntax.Node.UnaryExpressionSyntax import UnaryExpressionSyntax
from Syntax.TokenKind import TokenKind


class Parser:
    def __init__(self, tokens: list[SyntaxToken], diagnostics: DiagnosticBag):
        self._pos: int = 0
        self._tokens: list[SyntaxToken] = tokens
        self._valid_token = self._current_token().kind != TokenKind.Invalid
        self._diagnostics: DiagnosticBag = diagnostics
        self.tree: SyntaxNode

    def _current_token(self):
        if self._pos >= 0 and self._pos < len(self._tokens):
            return self._tokens[self._pos]

        else:
            return SyntaxToken(TokenKind.Invalid, self._pos, 0)

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
        return SyntaxToken(token_kinds[0], self._current_token().pos, self._current_token().length)

    def parse(self):
        self.tree = self._parse_equation()
        self._expect_kind(TokenKind.End)

    def _parse_equation(self):
        left = self._parse_expression()

        while self._current_token().kind == TokenKind.Equal:
            operator = self._advance()
            right = self._parse_expression()
            left = EquationSyntax(left, operator, right)

        return left

    def _parse_expression(self):
        return self._parse_binary_expression()

    def _parse_binary_expression(self, operator_precedence = SyntaxToken.MAX_PRECEDENCE):
        if operator_precedence == 0:
            return self._parse_unary_expression()

        left = self._parse_binary_expression(operator_precedence - 1)

        while self._current_token().precedence() == operator_precedence:
            operator = SyntaxToken(TokenKind.Star, self._current_token().pos, 0) if operator_precedence == SyntaxToken.IMPLICIT_MULT_PRECEDENCE else self._advance()
            right = self._parse_binary_expression(operator_precedence - 1)
            left = BinaryExpressionSyntax(left, operator, right)

        return left

    def _parse_unary_expression(self):
        if self._current_token().kind == TokenKind.Plus or self._current_token().kind == TokenKind.Minus:
            operator = self._advance()
            right = self._parse_unary_expression()

            return UnaryExpressionSyntax(operator, right)

        return self._parse_primary()

    def _parse_primary(self):
        current_token = self._current_token()

        if current_token.kind == TokenKind.FunctionName:
            return self._parse_function()

        elif (current_token.kind == TokenKind.LParen):
            l_paren = self._advance()
            expr = self._parse_expression()
            r_paren = self._expect_kind(TokenKind.RParen)

            return ParenthesizedExpressionSyntax(l_paren, expr, r_paren)

        elif current_token.kind == TokenKind.Number:
            return NumberSyntax(self._advance())

        elif current_token.kind == TokenKind.Literal:
            return LiteralSyntax(self._advance())

        else:
            if self._valid_token:
                self._diagnostics.append(UnexpectedToken(self._current_token()))
            return InvalidSyntax(self._advance())

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

        return FunctionSyntax(function_name, l_paren, args, r_paren)
