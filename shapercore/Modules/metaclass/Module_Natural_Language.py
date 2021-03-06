from abc import abstractmethod
from shapercore.Modules.metaclass.Module import Module


class Data(metaclass=Module):
    def __init__(self):
        pass

    @abstractmethod
    def function(self):
        pass

    @abstractmethod
    def requirement(self):
        """ Apply function only on non-numeric values"""
        pass

    @abstractmethod
    def unit_test(self):
        pass

    @abstractmethod
    def execute(self):
        pass
