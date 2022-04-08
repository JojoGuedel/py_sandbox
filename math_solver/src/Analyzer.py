from Syntax.Lexer import Lexer
from Syntax.Parser import Parser


class Analyzer:
    def __init__(self):
        pass
    
    def analyze(self, text: str) -> ParserNode:
        lexer = Lexer(self._text)
        lexer.lex()

        parser = Parser(self._lexer.tokens)
        parser.parse()
        
        lowerer = Lowerer(self._text, parser.syntaxTree)