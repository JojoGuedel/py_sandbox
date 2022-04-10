from tokenize import Token
from Syntax.Node.SyntaxNode import SyntaxNode


class UnaryExpressionSyntax(SyntaxNode):
    def __init__(self, operator: Token, right: SyntaxNode):
        self.operator = operator
        self.right = right
            
    def children(self):
        return [self.operator, self.right]