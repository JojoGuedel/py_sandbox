from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def children(self):
        pass    

    @abstractmethod
    def summands(self):
        pass

    @abstractmethod
    def factors(self):
        pass
    
    def __str__(self):
        return self.__class__.__name__
    
    def __repr__(self) -> str:
        return str(self)