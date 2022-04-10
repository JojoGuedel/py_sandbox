from Syntax.Node.SyntaxToken import SyntaxToken
from Syntax.Node.SyntaxNode import SyntaxNode

class FunctionSyntax(SyntaxNode):
    def __init__(self, function_name: SyntaxToken, l_paren: SyntaxNode, args: list[SyntaxNode], r_paren: SyntaxToken):
        self.function_name = function_name
        self.l_paren = l_paren
        self.args = args
        self.r_paren = r_paren
            
    def children(self):
        return [self.function_name, self.l_paren, *self.args, self.r_paren]