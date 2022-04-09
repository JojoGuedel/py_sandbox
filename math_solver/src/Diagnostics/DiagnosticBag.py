from Diagnostics.DiagnosticKind import DiagnosticKind


class DiagnosticBag:
    def __init__(self, text):
        self.text = text
        self.diagnostics: list[DiagnosticKind] = []
    
    def any(self):
        return len(self.diagnostics) > 0

    def append(self, diagnostic: DiagnosticKind):
        self.diagnostics.append(diagnostic)
    
    def print(self):
        for d in self.diagnostics:
            print(self.text)
            print(" " * d.pos + "~" * d.length)
            print(d.msg, end="\n\n")