from Syntax.TokenKind import TokenKind


class Token:
    def __init__(self, kind: TokenKind, pos, len):
        self.kind = kind
        self.pos = pos
        self.len = len

    def __str__(self):
        return f"{self.kind}({self.pos}:{self.len})"
    
    def __repr__(self):
        return str(self)