class DatasetResult():
    def __init__(self,datasetName,ranker,results):
        self.datasetName = datasetName
        self.ranker = ranker
        self.results = results

    def toHTML(self):
        result = "<tr><td>" + self.datasetName + "</td><td>" + self.ranker.getName() + "</td>"
        for measure in self.results:
            result += "<td>" + str(measure.result) + "</td>";
        result += "</tr>";
        return result
