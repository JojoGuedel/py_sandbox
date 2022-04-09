from Syntax.Node.SyntaxNode import SyntaxNode
from Syntax.Node.Token import Token


class Literal(SyntaxNode):
    def __init__(self, token: Token):
        self.token = token

    def children(self):
        return [self.token]