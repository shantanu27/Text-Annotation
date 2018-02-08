import sys

class MaxCombiner():
    def getName( self ):
        return "MAX";

    def combineScores( self , scoreList ):
        max = float(0)
        for score in scoreList:
            if ( score > max ): 
                max = score
        return max;
