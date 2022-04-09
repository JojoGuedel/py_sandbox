from Syntax.TokenKind import TokenKind


class Token:
    MAX_PRECEDENCE = 4

    def __init__(self, kind: TokenKind, pos: int, len: int):
        self.kind = kind
        self.pos = pos
        self.len = len

        self.get_precedence()

    def __str__(self):
        return f"{self.kind}({self.pos}:{self.len})"
    
    def __repr__(self):
        return str(self)
    
    def get_precedence(self):
        if self.kind == TokenKind.Star or self.kind == TokenKind.Slash:
            return 1

        elif self.kind == TokenKind.Plus or self.kind == TokenKind.Minus:
            return 2

        return -1
