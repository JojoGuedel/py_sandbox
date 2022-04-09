from Diagnostics.DiagnosticKind import DiagnosticKind


class InvalidChar(DiagnosticKind):
    @property
    def pos(self): return self._pos

    @property
    def length(self): return self._length
    
    @property
    def msg(self): return self._msg

    def __init__(self, pos: int, length: int, char: str):
        self._pos = pos
        self._length = length
        self._msg = f"invalid char '{char}'"