class DataElement():
    def __init__(self,questionText,answerList):
        self.questionText = str(questionText)
        self.answerList = list()
        self.answerList.extend(answerList)

