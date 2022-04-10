from Evaluation.Node.Expression import Expression


class NumberExpression(Expression):
    def __init__(self, value):
        self.value = value

    def children(self):
        return [self]    

    def summands(self):
        return [self]

    def factors(self):
        return [self]
        
    def __str__(self):
        return f"{self.__class__.__name__}: {self.value}"