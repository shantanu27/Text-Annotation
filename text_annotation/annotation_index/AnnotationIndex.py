from abc import abstractmethod


class AnnotationIndex:

    @abstractmethod
    def add_annotation(self, annotation_type, begin, end):
        pass

    @abstractmethod
    def get_annotations(self, annotation_type, begin, end):
        pass
