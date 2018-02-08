import sys
from SetRanker import SetRanker

class AnswerCoverageRanker(SetRanker):
    def doSetRanking(self):
        intersectionSize = len( self.intersection )
        answerSize = len( self.answerTerms )
        return float(intersectionSize)  / float(answerSize) 

    def getName(self):
        return "AnswerCoverageRanker"

if __name__ == '__main__':
    question = sys.argv[1]
    answer = sys.argv[2]
    ranker = AnswerCoverageRanker();
    print(ranker.rankAnswer(question,answer))
