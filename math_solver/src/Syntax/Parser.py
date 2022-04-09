from Syntax.Token import Token
from Syntax.TokenKind import TokenKind

class ParserNode:
    def get_childrens():
        pass

class EquationParserNode(ParserNode):
    def __init__(self, left: ParserNode, op: Token, right: ParserNode):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"{__class__.__name__}({str(self.left)} [=] {str(self.right)})"

    def __repr__(self):
        return str(self)
        
    def get_childrens(self):
        return [self.left, self.op, self.right]

class BinaryExpressionParserNode(ParserNode):
    def __init__(self, left: ParserNode, op: Token, right: ParserNode):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"{__class__.__name__}({str(self.left)}, {str(self.op)}, {str(self.right)})"

    def __repr__(self):
        return str(self)   

    def get_childrens(self):
        return [self.left, self.op, self.right]

class UnaryExpressionParserNode(ParserNode):
    def __init__(self, op: Token, right: ParserNode):
        self.op = op
        self.right = right

    def __str__(self):
        return f"{__class__.__name__}({str(self.op)}, {str(self.right)})"

    def __repr__(self):
        return str(self)
            
    def get_childrens(self):
        return [self.op, self.right]

class ParenthesizedExpressionParserNode(ParserNode):
    def __init__(self, l_paren: Token, expr: ParserNode, r_paren: Token):
        self.l_paren = l_paren
        self.expr = expr
        self.r_paren = r_paren

    def __str__(self):
        return f"{__class__.__name__}({str(self.expr)})"

    def __repr__(self):
        return str(self)
            
    def get_childrens(self):
        return [self.l_paren, self.expr, self.r_paren]

class FunctionParserNode(ParserNode):
    def __init__(self, function_name: Token, l_paren: Token, args: list[ParserNode], r_paren: Token):
        self.function_name = function_name
        self.l_paren = l_paren
        self.args = args
        self.r_paren = r_paren

    def __str__(self):
        s = f"{__class__.__name__}({self.function_name}("

        for i in self.args:
            s += f"{str(i)}, "

        return s[:-2] + ")"

    def __repr__(self):
        return str(self)
            
    def get_childrens(self):
        ret = [self.function_name, self.l_paren]
        ret.extend(self.args)
        ret.append(self.r_paren)
        return ret

class NumberParserNode(ParserNode):
    def __init__(self, token: Token):
        self.token = token

    def __str__(self):
        return f"{__class__.__name__}({self.token})"

    def __repr__(self):
        return str(self)
        
    def get_childrens(self):
        return [self.token]

class LiteralParserNode(ParserNode):
    def __init__(self, token: Token):
        self.token = token

    def __str__(self):
        return f"{__class__.__name__}({self.token})"

    def __repr__(self):
        return str(self)
        
    def get_childrens(self):
        return [self.token]

class InvalidParserNode(ParserNode):
    def __init__(self, token: Token):
        self.token = token

    def __str__(self):
        return f"{__class__.__name__}({self.token})"

    def __repr__(self):
        return str(self)
        
    def get_childrens(self):
        return [self.token]

class Parser:
    _pos: int
    _tokens: list[Token]
    tree: ParserNode

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

            return EquationParserNode(left, op, right)

        return left

    def _parse_binary_expression(self, operator_precedence = Token.MAX_PRECEDENCE):
        if operator_precedence == 0:
            return self._parse_unary_expression()

        left = self._parse_binary_expression(operator_precedence - 1)

        while self._current_token().get_precedence() == operator_precedence:
            op = self._advance()
            right = self._parse_binary_expression(operator_precedence - 1)
            left = BinaryExpressionParserNode(left, op, right)

        return left

    def _parse_unary_expression(self):
        if self._current_token().kind == TokenKind.Plus or self._current_token().kind == TokenKind.Minus:
            op = self._advance()
            right = self._parse_unary_expression()

            return UnaryExpressionParserNode(op, right)

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
            return BinaryExpressionParserNode(left, op, right)

        return left

    def _parse_primary(self):
        current_token = self._current_token()

        if current_token.kind == TokenKind.FunctionName:
            return self._parse_function()

        elif (current_token.kind == TokenKind.LParen):
            l_paren = self._advance()
            expr = self._parse_expression()
            r_paren = self._expect_kind(TokenKind.RParen)

            return ParenthesizedExpressionParserNode(l_paren, expr, r_paren)

        elif current_token.kind == TokenKind.Number:
            return NumberParserNode(self._advance())

        elif current_token.kind == TokenKind.Literal:
            return LiteralParserNode(self._advance())

        else:
            # TODO: add diagnostics
            return InvalidParserNode(self._advance())

    def _parse_function(self):
        function_name = self._advance()
        l_paren = self._expect_kind(TokenKind.LParen)

        args: list[ParserNode] = []
        if self._current_token().kind != TokenKind.RParen:
            args.append(self._parse_expression())

            while self._current_token().kind == TokenKind.Comma:
                self._pos += 1
                args.append(self._parse_expression())

        r_paren = self._expect_kind(TokenKind.RParen)

        return FunctionParserNode(function_name, l_paren, args, r_paren)
