import sys
from SetRanker import SetRanker

class JaccardRanker(SetRanker):
    def doSetRanking(self):
        intersectionSize = len( self.intersection )
        totalSize = len ( self.union )
        return float(intersectionSize)/float(totalSize)

    def getName(self):
        return "JaccardRanker"

if __name__ == '__main__':
    question = sys.argv[1]
    answer = sys.argv[2]
    ranker = JaccardRanker();
    print(ranker.rankAnswer(question,answer))
