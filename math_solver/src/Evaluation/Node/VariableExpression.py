from unicodedata import name
from Evaluation.Node.Expression import Expression


class VariableExpression(Expression):
    def __init__(self, name: str):
        self.name = name

    def children(self):
        return [self]

    def summands(self):
        return [self]

    def factors(self):
        return [self]
    
    def __str__(self):
        return f"{self.__class__.__name__}: '{self.name}'"