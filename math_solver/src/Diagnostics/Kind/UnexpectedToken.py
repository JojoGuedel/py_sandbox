from Diagnostics.DiagnosticKind import DiagnosticKind
from Syntax.Node.SyntaxToken import SyntaxToken
from Syntax.TokenKind import TokenKind


class UnexpectedToken(DiagnosticKind):
    @property
    def pos(self): return self._pos

    @property
    def length(self): return self._length
    
    @property
    def msg(self): return self._msg

    def __init__(self, token: SyntaxToken, expected_kind: TokenKind = None):
        self._pos = token.pos
        self._length = token.length
        self._msg = f"unexpected token '{token.kind}'" + (f", expected '{expected_kind}'" if not expected_kind is None else "")
