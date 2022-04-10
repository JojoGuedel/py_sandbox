from Evaluation.Node.ComposedExpression import ComposedExpression


class Equation(ComposedExpression):
    def __init__(self, *exprs):
        self._exprs = []
        self._exprs.extend(exprs)
    
    def append(self, expr):
        self._exprs.append(expr)

    def children(self):
        return self._expr