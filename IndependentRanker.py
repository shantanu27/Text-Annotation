import abc
from abc import abstractmethod

class IndependentRanker():
    __metaclass__ = abc.ABCMeta
    @abstractmethod
    def rankAnswer(self, question, answer):
        pass
    @abstractmethod
    def getName(self):
        pass

