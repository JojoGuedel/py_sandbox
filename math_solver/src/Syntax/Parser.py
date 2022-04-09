from Syntax.Invalid import Invalid
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
    _pos: int
    _tokens: list[Token]
    tree: SyntaxNode

    def __init__(self, tokens: list[Token]):
        self._pos = 0
        self._tokens = tokens

    def _current_token(self):
        if self._pos >= 0 and self._pos < len(self._tokens):
            return self._tokens[self._pos]

        else:
            return Token(TokenKind.Invalid, self._pos, 0)

    def _advance(self):
        token = self._current_token()
        self._pos += 1
        return token

    def _expect_kind(self, *token_kinds: TokenKind):
        if len(token_kinds) < 1:
            # TODO: log internal error
            return

        current_token = self._current_token()

        for token_kind in token_kinds:
            if current_token.kind == token_kind:
                return self._advance()

        # TODO: add diagnostics
        return Token(token_kinds[0], self._current_token().pos, self._current_token().len)

    def parse(self):
        self.tree = self._parse_expression()
        self._expect_kind(TokenKind.End)

    def _parse_expression(self):
        return self._parse_equation()

    def _parse_equation(self):
        left = self._parse_binary_expression()

        # TODO: move this to primary?
        if self._current_token().kind == TokenKind.Equal:
            op = self._advance()
            right = self._parse_expression()

            return Equation(left, op, right)

        return left

    def _parse_binary_expression(self, operator_precedence = Token.MAX_PRECEDENCE):
        if operator_precedence == 0:
            return self._parse_unary_expression()

        left = self._parse_binary_expression(operator_precedence - 1)

        while self._current_token().precedence() == operator_precedence:
            op = self._advance()
            right = self._parse_binary_expression(operator_precedence - 1)
            left = BinaryExpression(left, op, right)

        return left

    def _parse_unary_expression(self):
        if self._current_token().kind == TokenKind.Plus or self._current_token().kind == TokenKind.Minus:
            op = self._advance()
            right = self._parse_unary_expression()

            return UnaryExpression(op, right)

        return self._parse_implicit_multiply()

    def _parse_implicit_multiply(self):
        left = self._parse_primary()

        if self._current_token().kind == TokenKind.FunctionName     or \
           self._current_token().kind == TokenKind.LParen           or \
           self._current_token().kind == TokenKind.Literal          or \
           self._current_token().kind == TokenKind.Number:

            op = Token(TokenKind.Star, self._current_token().pos, 0)
            right = self._parse_unary_expression()

            # TODO: differenciate this from binary expression for esthetics
            return BinaryExpression(left, op, right)

        return left

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
            # TODO: add diagnostics
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
