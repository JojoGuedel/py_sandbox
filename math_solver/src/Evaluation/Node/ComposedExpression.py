from abc import ABC, abstractmethod


class ComposedExpression(ABC):
    @abstractmethod
    def append(self, expr):
        pass

    @abstractmethod
    def extend(self, expr_list):
        pass