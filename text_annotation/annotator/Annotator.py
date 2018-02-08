from abc import abstractmethod


class Annotator:

    def __init__(self, name):
        self.name = name

    def process(self, annotated_string, begin=0, end=None):
        if end is None:
            end = len(annotated_string.text)
        indexes = self.generate_annotation_index(annotated_string, begin, end)
        for index in indexes:
            annotated_string.index.add_annotation(index.annotation_type, index.begin, index.end)

    @abstractmethod
    def generate_annotation_index(self, annotated_string, begin, end):
        pass
