from abc import ABC, abstractproperty
from Syntax.Node.SyntaxToken import SyntaxToken
from Syntax.TokenKind import TokenKind

class DiagnosticKind(ABC):
    @abstractproperty
    def pos(): pass

    @abstractproperty
    def length(self): pass

    @abstractproperty
    def msg(self): pass
    