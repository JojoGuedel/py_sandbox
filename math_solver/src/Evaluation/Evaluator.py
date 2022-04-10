from Evaluation.Node.Expression import Expression
from Evaluation.Node.MultExpression import MultExpression
from Evaluation.Simplifier import Simplifier


class Evaluator:
    def __init__(self):
        pass

    def mult(self, left: Expression, right: Expression):
        return Simplifier(MultExpression(left, right)).simplify()

