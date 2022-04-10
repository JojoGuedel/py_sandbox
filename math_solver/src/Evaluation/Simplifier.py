from Evaluation.Node.AddExpression import AddExpression
from Evaluation.Node.Expression import Expression
from Evaluation.Node.MultExpression import MultExpression
from Evaluation.Node.NumberExpression import NumberExpression


class Simplifier:
    def __init__(self, expr: Expression):
        self._expr = expr

    def flatten(self):
        return self._flatten_expression(self._expr)
    
    def _flatten_expression(self, expr: Expression):
        flattened_expr: Expression

        if isinstance(expr, MultExpression):
            flattened_expr = AddExpression(NumberExpression(1))

            for child in expr.factors():
                new_flattened_expr = AddExpression()

                for child_summand in child.summands():
                    for flattened_expr_summand in flattened_expr.summands():
                        new_flattened_expr.append(MultExpression(*child_summand.factors(), *flattened_expr_summand.factors()))
                
                flattened_expr = new_flattened_expr
        
        elif isinstance(expr, AddExpression):
            flattened_expr = AddExpression()

            for i in expr.summands():
                child = self._flatten_expression(i)
                flattened_expr.extend(child.summands())
        
        else:
            flattened_expr = expr
        
        return flattened_expr

    def simplify(self):
        return self._simplify_expression(self._expr)
    
    def _simplify_expression(self, expr: Expression):
        if len(expr.children() == 1):
            return expr.children()[0]

        if isinstance(expr, MultExpression):
            pass