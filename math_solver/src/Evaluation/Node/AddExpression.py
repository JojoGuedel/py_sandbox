from Evaluation.Node.ComposedExpression import ComposedExpression
from Evaluation.Node.Expression import Expression
from Evaluation.Node.NumberExpression import NumberExpression
from Evaluation.Node.VariableExpression import VariableExpression


class AddExpression(Expression, ComposedExpression):
    def __init__(self, *exprs):
        self._children = []
        self._children.extend(exprs)

    def append(self, expr: Expression):
        self._children.append(expr)
    
    def extend(self, expr_list):
        self._children.extend(expr_list)

    def children(self):
        return self._children

    def summands(self):
        summands = []

        for i in self._children:
            summands.extend(i.summands())

        return summands

    def factors(self):
        return [self]