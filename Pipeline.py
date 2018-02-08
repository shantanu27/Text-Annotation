import abc
import sys
import time
from abc import abstractmethod
from AnswerCandidate import AnswerCandidate
from DataElement import DataElement
from DatasetResult import DatasetResult
from DatasetMeasure import DatasetMeasure
from CompositeRanker import CompositeRanker
from MaxCombiner import MaxCombiner
from MinCombiner import MinCombiner
from MeanCombiner import MeanCombiner
from JaccardRanker import JaccardRanker
from ShantaRanker import ShantaRanker
from QuestionCoverageRanker import QuestionCoverageRanker
from AnswerCoverageRanker import AnswerCoverageRanker
from RankedAnswer import RankedAnswer

class Pipeline():
    __metaclass__ = abc.ABCMeta
    @classmethod
    def readDataset(self,datasetFile):
        infile = open(datasetFile,'r')
        dataset = list()

        answerList = list()
        for line in infile:
            line = line[:-1]
            columnValues = line.split(',')
            lineType = columnValues[0]
            if lineType == "Q":
                if (len(answerList) > 0):
                    dataElement = DataElement(questionText,answerList)
                    dataset.append(dataElement)                    
                    answerList = list()
                questionText = columnValues[1]
            if lineType == "A":
                answerFlag = columnValues[1]
                answerText = columnValues[2]
                answerCandidate = AnswerCandidate(answerFlag,answerText)
                answerList.append(answerCandidate)
        if (len(answerList) > 0):
            dataElement = DataElement(questionText,answerList)
            dataset.append(dataElement)                    
        return dataset

    @classmethod
    def processDataset(self,datasetFile,ranker):
        cols = datasetFile.split(".")
        outfilename = "logs/" + cols[0] + "." + ranker.getName() + ".log"
        outfile = open( outfilename ,"w")
        dataset = self.readDataset(datasetFile)
        scoreAccumulator = float(0)
        mrrAccumulator = float(0)
        for element in dataset:
            questionText = element.questionText
            rankedList = list()
            outfile.write("\n" + questionText + "\n" )
            answerList = element.answerList
            for answerCandidate in answerList:
                answerText = answerCandidate.answerText
                answerScore = ranker.rankAnswer(questionText,answerText)
                rankedElement = RankedAnswer( answerScore , answerCandidate )
                rankedList.append( rankedElement )
            sortedRankedList = sorted(rankedList, key=lambda rankedAnswer: rankedAnswer.answerScore , reverse=True)
            correctCount = 0
            rank = 0
            foundRank = 0
            for rankedAnswer in sortedRankedList:
                rank += 1
                outfile.write( rankedAnswer.answerCandidate.answerFlag + " " + format(rankedAnswer.answerScore,'.4f') + " " + rankedAnswer.answerCandidate.answerText + "\n" )
                if rankedAnswer.answerCandidate.answerFlag == "1":
                    correctCount += 1
                    if foundRank == 0: 
                        foundRank = rank
            correctFound = 0
            if correctCount > 0:
                for rankedAnswer in sortedRankedList[0:correctCount]:
                    if rankedAnswer.answerCandidate.answerFlag == "1":
                        correctFound += 1;
            correctScore = float(0);
            if ( correctCount > 0 ):
                correctScore = float(correctFound) / float(correctCount)
            outfile.write("\nP@N: "  + repr(correctFound) + " out of top " + repr(correctCount) + " = " + format(correctScore,'.4f') + "\n" )
            scoreAccumulator += correctScore;
            mrr = 0;
            if foundRank > 0:
                mrr = 1 / foundRank
            outfile.write("\nMRR: "  + repr(mrr)  + "\n" )
            mrrAccumulator += mrr;
        macroScore = scoreAccumulator / float(len(dataset))
        macroMeasure = DatasetMeasure( "P@N" , macroScore )
        macroMRR = mrrAccumulator / float(len(dataset))
        MRRMeasure = DatasetMeasure( "MRR" , macroMRR )
        outfile.write ("\nMacro averaged score (" + ranker.getName() +"): " + format(macroScore,'.3f') + "\n" )
        outfile.write ("\nMacro averaged MRR (" + ranker.getName() +"): " + format(macroMRR,'.3f') + "\n" )
        outfile.close()
        measures = list()
        # Note: results table sorted by the first measure in the list
        measures.append( MRRMeasure )
        measures.append( macroMeasure )
        return measures

    @classmethod
    def generateTable(self,testName,sortedResultList):
        ts = time.gmtime()
        tsf = time.strftime("%Y-%m-%d %H:%M:%S", ts)
        table = "<html><head><title>"+ testName + " " + tsf + "</title><link href=\"results.css\" rel=\"stylesheet\"></head><body><h2>" + tsf + " " + testName + "</h2>\n<table>\n<tr><th>Dataset</th><th>Ranker</th>" 
        example = sortedResultList[0];
        results = example.results;
        for result in results:
            table += "<th>" + result.measureName + "</th>"
        table += "</tr>"
        for datasetResult in sortedResultList:
            table += datasetResult.toHTML() + "\n"
        table += "</table>\n</body>\n</html>\n";
        return table

if __name__ == '__main__':
    pipeline = Pipeline()

    datasets = list()
    datasets.append( "dataset_001.csv" )
    datasets.append( "dataset_002.csv" )
    datasets.append( "dataset_003.csv" )
    datasets.append( "dataset_004.csv" )

    rankers = list()
    rankers.append( JaccardRanker() )
    rankers.append( QuestionCoverageRanker() )
    rankers.append( AnswerCoverageRanker() )
    rankers.append(ShantaRanker())

    compositeRankers = list()
    compositeRankers.append( CompositeRanker( MaxCombiner()  ) )
    compositeRankers.append( CompositeRanker( MinCombiner()  ) )
    compositeRankers.append( CompositeRanker( MeanCombiner() ) )
    for composite in compositeRankers:
        composite.addRanker( JaccardRanker() )
        composite.addRanker( QuestionCoverageRanker() )
        composite.addRanker( AnswerCoverageRanker() )
        composite.addRanker(ShantaRanker())

    datasetResults = list()

    for dataset in datasets:
        datasetNameFields = dataset.split(".")
        datasetName = datasetNameFields[0]
        for ranker in rankers:
            result = pipeline.processDataset( dataset , ranker )
            datasetResult = DatasetResult(datasetName,ranker,result)
            datasetResults.append(datasetResult)
        for composite in compositeRankers:        
            result = pipeline.processDataset( dataset , composite )
            datasetResult = DatasetResult(datasetName,composite,result)
            datasetResults.append(datasetResult)

    sortedResultList = sorted(datasetResults, key=lambda datasetResult: datasetResult.results[0].result , reverse=True)
    table = pipeline.generateTable("Pipeline.py",sortedResultList)

    outfile = open("resultsTable.html","w")
    outfile.write( table );
    outfile.close();




