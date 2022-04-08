from ast import UnaryOp
from lib2to3.pgen2 import token
from re import L
from turtle import right
from Syntax.Token import Token
from src.Syntax.TokenKind import TokenKind

class ParserNode:
    pass

class EquationParserNode(ParserNode):
    def __init__(self, left: ParserNode, op: Token, right: ParserNode):
        self._left = left
        self._op = op
        self._right = right

class BinaryExpressionParserNode(ParserNode):
    def __init__(self, left: ParserNode, op: Token, right: ParserNode):
        self._left = left
        self._op = op
        self._right = right

class UnaryExpressionParserNode(ParserNode):
    def __init__(self, op: Token, right: ParserNode):
        self._op = op
        self._right = right

class ParenthesizedExpressionParserNode(ParserNode):
    def __init__(self, l_paren: Token, expr: ParserNode, r_paren: Token):
        self._l_paren = l_paren
        self._expr = expr
        self._r_paren = r_paren

class NumberParserNode(ParserNode):
    pass

class InvalidParserNode(ParserNode):
    def __init__(self, token: Token):
        pass

class Parser:
    _pos: int
    _tokens: list[Token]
    _parser_tree: ParserNode

    def __init__(self, tokens: list[Token]):
        self._pos = 0
        self._tokens = token

    def _current_token(self):
        if self._pos >= 0 and self._pos < len(self._tokens):
            return self._tokens[self._pos]
        
        else:
            return Token(TokenKind.Invalid, self._pos, 0)
    
    def _advance(self):
        token = self._current_token()
        pos += 1
        return token
    
    def _expect_kind(self, token_kind: TokenKind):
        if self._current_token().kind == TokenKind:
            return self._current_token()
        
        # TODO: add diagnostics
        return Token(token_kind, self._current_token().pos, self._current_token().len)

    def parse(self):
        self._parser_tree = self._parse_expression
    
    def _parse_expression(self):
        return self._parse_equation()

    def _parse_equation(self):
        left = self._advance()

        if self._current_token().kind == TokenKind.Equal:
            pos += 1
            right = self._parse_expression()

            return EquationParserNode(left, right)
        
        return left

    def _parse_binary_expression(self, operator_precedence = 10):
        if operator_precedence == 0:
            return self._parse_unary_expression()
    
    def _parse_unary_expression(self):
        if self._current_token().kind == TokenKind.Plus or self._current_token().kind == TokenKind.Minus:
            op = self._advance
            right = self._parse_expression()

            return UnaryExpressionParserNode(op, right)
        
        return
    
    def _parse_primary(self):
        if (self._current_token().kind == TokenKind.LParen):
            l_paren = self._advance()
            expr = self._parse_expression()
            r_paren = self._expect_kind(TokenKind.RParen)

            return ParenthesizedExpressionParserNode(l_paren, expr, r_paren)
        
        else:
            return InvalidParserNode(self._current_token)
