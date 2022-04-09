from tokenize import Token
from Syntax.Node.SyntaxNode import SyntaxNode


class ParenthesizedExpression(SyntaxNode):
    def __init__(self, l_paren: Token, expr: SyntaxNode, r_paren: Token):
        self.l_paren = l_paren
        self.expr = expr
        self.r_paren = r_paren

    def children(self):
        return [self.l_paren, self.expr, self.r_paren]