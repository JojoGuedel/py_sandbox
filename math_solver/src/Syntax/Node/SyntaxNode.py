from abc import ABC, abstractmethod


class SyntaxNode(ABC):
    def __str__(self):
        return f"{__class__.__name__}"
    
    def __repr__(self):
        return str(self)

    @abstractmethod
    def children(self):
        pass
