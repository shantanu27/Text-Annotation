

class Annotation:

    def __init__(self, annotation_type, begin, end):
        self.annotation_type = annotation_type
        self.begin = begin
        self.end = end

    def __str__(self):
        return "[" + self.annotation_type + " " + str(self.begin) + " " + str(self.end) + "]"
