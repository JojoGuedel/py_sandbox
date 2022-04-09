from Syntax.Node.Token import Token
from Syntax.Node.SyntaxNode import SyntaxNode


class Arguments(SyntaxNode):
    def __init__(self, args: list [SyntaxNode]):
        self.args = args
    
    def children(self):
        return []

class Function(SyntaxNode):
    def __init__(self, function_name: Token, l_paren: SyntaxNode, args: Arguments, r_paren: Token):
        self.function_name = function_name
        self.l_paren = l_paren
        self.args = args
        self.r_paren = r_paren
            
    def children(self):
        return [self.function_name, self.l_paren, *self.args, self.r_paren]