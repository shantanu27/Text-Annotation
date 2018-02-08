import sys
from abc import abstractmethod
from IndependentRanker import IndependentRanker
from MaxCombiner import MaxCombiner
from MinCombiner import MinCombiner
from MeanCombiner import MeanCombiner
from JaccardRanker import JaccardRanker
from QuestionCoverageRanker import QuestionCoverageRanker
from AnswerCoverageRanker import AnswerCoverageRanker

class CompositeRanker(IndependentRanker):
    def __init__(self,combiner):
        self.rankers = list()
        self.combiner = combiner;

    def rankAnswer(self, question, answer):
        scoreList = list()
        for ranker in self.rankers:
            scoreList.append( ranker.rankAnswer(question,answer) )
        return self.combiner.combineScores( scoreList );

    def addRanker(self, ranker):
        self.rankers.append( ranker );

    def getName(self):
        result = self.combiner.getName() + "."
        for  ranker in self.rankers:
            result += ranker.getName()
            result += "." 
        result = result[0:-1]
        return result;

if __name__ == '__main__':
    question = sys.argv[1]
    answer = sys.argv[2]
    rankers = list()
    rankers.append( CompositeRanker( MaxCombiner() )  )
    rankers.append( CompositeRanker( MinCombiner() )  )
    rankers.append( CompositeRanker( MeanCombiner() ) )
    print( question )
    print( answer )
    for composite in rankers:
        composite.addRanker( JaccardRanker() )
        composite.addRanker( QuestionCoverageRanker() )
        composite.addRanker( AnswerCoverageRanker() )
        print( composite.getName() )
        print( composite.rankAnswer( question , answer ) );
