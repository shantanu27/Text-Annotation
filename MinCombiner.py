import sys

class MinCombiner():
    def getName( self ):
        return "MIN";

    def combineScores( self , scoreList ):
        min = float('inf')
        for score in scoreList:
            if ( score < min ): 
                min = score
        return min;
