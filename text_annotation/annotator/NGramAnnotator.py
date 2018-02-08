from text_annotation.Annotation import Annotation
from .Annotator import Annotator


class NGramAnnotator(Annotator):

    def __init__(self, n, annotation_type, name):
        super().__init__(name)
        self.n = n
        self.annotation_type = annotation_type

    def generate_annotation_index(self, annotated_string, begin, end):
        a = annotated_string.index.get_annotations(self.annotation_type, begin, end)
        indexes = list()
        for i in range(0, len(a)-self.n+1):
            annotation = Annotation(self.name, a[i].begin, a[i+self.n-1].end)
            indexes.append(annotation)
        return indexes
