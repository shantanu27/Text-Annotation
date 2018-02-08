from abc import abstractmethod
from IndependentRanker import IndependentRanker

class SetRanker(IndependentRanker):

    def rankAnswer(self, question, answer):
        self.questionTerms = set(question.split(' '))
        self.answerTerms   = set(answer.split(' '))
        self.intersection = self.answerTerms.intersection(self.questionTerms)
        self.union = self.answerTerms.union(self.questionTerms)
        self.answerDifference  = self.answerTerms.difference(self.questionTerms)
        self.questionDifference  = self.questionTerms.difference(self.answerTerms)
        return self.doSetRanking();

    @abstractmethod
    def doSetRanking(self):
        pass



