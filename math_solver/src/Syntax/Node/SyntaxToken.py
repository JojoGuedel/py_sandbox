from Syntax.Node.SyntaxNode import SyntaxNode
from Syntax.TokenKind import TokenKind


class SyntaxToken(SyntaxNode):
    IMPLICIT_MULT_PRECEDENCE = 1
    MAX_PRECEDENCE = 3

    def __init__(self, kind: TokenKind, pos: int, length: int):
        self.kind = kind
        self.pos = pos
        self.length = length

    def __str__(self):
        return f"{self.kind}({self.pos}:{self.length})"
    
    def children(self):
        return []
    
    def precedence(self):
        if self.kind == TokenKind.FunctionName   or \
           self.kind == TokenKind.LParen         or \
           self.kind == TokenKind.Literal        or \
           self.kind == TokenKind.Number:
           return 1

        if self.kind == TokenKind.Star or self.kind == TokenKind.Slash:
            return 2

        elif self.kind == TokenKind.Plus or self.kind == TokenKind.Minus:
            return 3

        return -1
