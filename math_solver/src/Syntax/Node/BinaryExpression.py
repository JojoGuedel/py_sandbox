from tokenize import Token
from Syntax.Node.SyntaxNode import SyntaxNode


class BinaryExpression(SyntaxNode):
    def __init__(self, left: SyntaxNode, operator: Token, right: SyntaxNode):
        self.left = left
        self.operator = operator
        self.right = right

    def children(self):
        return [self.left, self.operator, self.right]