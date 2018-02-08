import sys
from SetRanker import SetRanker

class QuestionCoverageRanker(SetRanker):
    def doSetRanking(self):
        intersectionSize = len( self.intersection )
        questionSize = len( self.questionTerms )
        return float(intersectionSize)  / float(questionSize)

    def getName(self):
        return "QuestionCoverageRanker"

if __name__ == '__main__':
    question = sys.argv[1]
    answer = sys.argv[2]
    ranker = QuestionCoverageRanker();
    print(ranker.rankAnswer(question,answer))
