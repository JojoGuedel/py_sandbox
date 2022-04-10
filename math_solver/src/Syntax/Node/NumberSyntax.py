from Syntax.Node.SyntaxNode import SyntaxNode
from Syntax.Node.SyntaxToken import SyntaxToken


class NumberSyntax(SyntaxNode):
    def __init__(self, token: SyntaxToken):
        self.token = token
        
    def children(self):
        return [self.token]