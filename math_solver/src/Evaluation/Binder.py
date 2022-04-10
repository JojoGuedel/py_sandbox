from decimal import Decimal
from Diagnostics.DiagnosticBag import DiagnosticBag
from Evaluation.Node.AddExpression import AddExpression
from Evaluation.Node.Equation import Equation
from Evaluation.Node.MultExpression import MultExpression
from Evaluation.Node.NumberExpression import NumberExpression
from Evaluation.Node.VariableExpression import VariableExpression
from Syntax.Node.BinaryExpressionSyntax import BinaryExpressionSyntax
from Syntax.Node.EquationSyntax import EquationSyntax
from Syntax.Node.LiteralSyntax import LiteralSyntax
from Syntax.Node.NumberSyntax import NumberSyntax
from Syntax.Node.ParenthesizedExpressionSyntax import ParenthesizedExpressionSyntax
from Syntax.Node.SyntaxNode import SyntaxNode
from Syntax.TokenKind import TokenKind


class Binder:
    def __init__(self, text: str, parser_tree: SyntaxNode):
        self.text = text
        self._parser_tree = parser_tree
        # self._diagnostics = diagnostics
    
    def bind(self):
        return self._bind(self._parser_tree)
    
    def _bind(self, expr: SyntaxNode):
        if isinstance(expr, EquationSyntax):
            return self._bind_equation(expr)
        
        elif isinstance(expr, BinaryExpressionSyntax):
            if expr.operator.kind == TokenKind.Plus:
                return AddExpression(self._bind(expr.left), self._bind(expr.right))

            elif expr.operator.kind == TokenKind.Minus:
                pass

            elif expr.operator.kind == TokenKind.Star:
                return MultExpression(self._bind(expr.left), self._bind(expr.right))

            elif expr.operator.kind == TokenKind.Slash:
                pass
        
        elif isinstance(expr, ParenthesizedExpressionSyntax):
            return self._bind(expr.expr)
        
        elif isinstance(expr, NumberSyntax):
            # TODO: prase the number a little bit more careful
            return NumberExpression(Decimal(self.text[expr.token.pos : expr.token.pos + expr.token.length]))
        
        elif isinstance(expr, LiteralSyntax):
            return VariableExpression(self.text[expr.token.pos : expr.token.pos + expr.token.length])
            
        else:
            pass

    def _bind_equation(self, expr: EquationSyntax, lvl = 0):
        exprs = []

        if isinstance(expr.left, EquationSyntax):
            exprs.append(self._bind_equation(expr.left, lvl + 1))
        else:
            exprs.append(self._bind(expr.left))

        if isinstance(expr.right, EquationSyntax):
            exprs.append(self._bind_equation(expr.right, lvl + 1))
        else:
            exprs.append(self._bind(expr.right))

        if lvl == 0:
            return Equation[exprs]
        else:
            return exprs