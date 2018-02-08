import sys

class MeanCombiner():
    def getName( self ):
        return "AVG";

    def combineScores( self , scoreList ):
        total = float(0)
        for score in scoreList:
            total += score
        return total / float(len( scoreList ))
