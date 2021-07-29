from abc import ABC

class Addable(ABC):
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Addable:
            if any("__add__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented