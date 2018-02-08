from Annotation import Annotation
from AnnotationIndex import AnnotationIndex


class ListAnnotationIndex(AnnotationIndex):

    def __init__(self):
        self.annotation_list = list()

    def add_annotation(self, annotation_type, begin, end):
        annotation = Annotation(annotation_type, begin, end)
        self.annotation_list.append(annotation)

    def get_annotations(self, annotation_type=None, begin=None, end=None):
        annotations = list()
        for annotation in self.annotation_list:
            if self.filter_annotation_type(annotation, annotation_type) and \
               self.filter_begin_end(annotation, begin, end):
                annotations.append(annotation)
        return annotations

    @staticmethod
    def filter_annotation_type(annotation, annotation_type):
        if annotation_type is not None:
            return annotation.annotation_type == annotation_type
        return True

    @staticmethod
    def filter_begin_end(annotation, begin, end):
        if begin is not None and end is not None:
            return annotation.begin >= begin and annotation.end <= end
        return True
