from Syntax.Node.SyntaxNode import SyntaxNode
from Syntax.TokenKind import TokenKind


class Token(SyntaxNode):
    MAX_PRECEDENCE = 2

    def __init__(self, kind: TokenKind, pos: int, len: int):
        self.kind = kind
        self.pos = pos
        self.len = len

    def __str__(self):
        return f"{self.kind}({self.pos}:{self.len})"
    
    def children(self):
        return []
    
    def precedence(self):
        if self.kind == TokenKind.Star or self.kind == TokenKind.Slash:
            return 1

        elif self.kind == TokenKind.Plus or self.kind == TokenKind.Minus:
            return 2

        return -1
