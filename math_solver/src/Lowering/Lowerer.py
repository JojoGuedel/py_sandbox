from abc import ABC, abstractmethod
from decimal import Decimal
from Diagnostics.DiagnosticBag import DiagnosticBag
from Syntax.Node.SyntaxNode import SyntaxNode

class IntermediateRepresentationNode(ABC):
    pass
    # @abstractmethod
    # def simplyfy(self):
    #     pass

class EquationNode(IntermediateRepresentationNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def children(self):
        return [self.left, self.right]

class ExpressionNode(IntermediateRepresentationNode):
    pass

class VariableNode(IntermediateRepresentationNode):
    def __init__(self, value: ExpressionNode):
        pass

class NumberNode(IntermediateRepresentationNode):
    def __init__(self, value: Decimal):
        self.value = value

    def prime_factor(self):
        pass

class FunctionNode(IntermediateRepresentationNode):
    pass


class Lowerer:
    def __init__(self, text: str, parser_tree: SyntaxNode, diagnostics: DiagnosticBag):
        self.text = text
        self._parser_tree = parser_tree
        self._diagnostics = diagnostics
    
    def lower(self):
        pass

    def _lower_expression(self):
        pass

    def _lower_equation(self):
        pass

    def _lower_binary_expression(self):
        pass

    def _lower_unary_exrpession(self):
        pass

    def _lower_function(self):
        pass

    def _lower_parenthesized_expression(self):
        pass

    def _lower_number(self):
        pass
    
    def _lower_literal(self):
        pass