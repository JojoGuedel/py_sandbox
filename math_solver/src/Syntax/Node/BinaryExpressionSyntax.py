from Syntax.Node.SyntaxNode import SyntaxNode
from Syntax.Node.SyntaxToken import SyntaxToken


class BinaryExpressionSyntax(SyntaxNode):
    def __init__(self, left: SyntaxNode, operator: SyntaxToken, right: SyntaxNode):
        self.left = left
        self.operator = operator
        self.right = right

    def children(self):
        return [self.left, self.operator, self.right]