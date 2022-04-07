from Syntax.Token import Token

class ParserNode:
    pass

class OperationNode:
    def __init__(self, operator: Token, childs: list[Token]):
        self._operator = operator
        self._childs = childs

class ParserNode:
    pass

class Parser:
    _parser_tree: ParserNode
    
    def __init__(self, tokens: list[Token]):
        pass

    def parse(self):
        pass

    def _parse_sum(self):
        pass
    
    def _parse_mlt(self):
        pass