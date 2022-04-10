from Diagnostics.DiagnosticBag import DiagnosticBag
from Evaluation.Binder import Binder
from Evaluation.Simplifier import Simplifier
from Syntax.Lexer import Lexer
from Syntax.Parser import Parser, SyntaxNode

class Analyzer:
    def __init__(self, text):
        self._text = text
    
    def analyze(self) -> SyntaxNode:
        self.diagnostics = DiagnosticBag(self._text)

        lexer = Lexer(self._text, self.diagnostics)
        lexer.lex()
        self.tokens = lexer.tokens

        parser = Parser(self.tokens, self.diagnostics)
        parser.parse()
        self.parser_tree = parser.tree
        
        binder = Binder(self._text, self.parser_tree)
        return Simplifier(binder.bind()).flatten()