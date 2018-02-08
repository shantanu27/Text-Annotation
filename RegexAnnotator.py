import re

from Annotation import Annotation
from Annotator import Annotator


class RegexAnnotator(Annotator):

    def __init__(self, name, regex):
        super().__init__(name)
        self.regex = regex
        self.re_compile = re.compile(regex)

    def generate_annotation_index(self, annotated_string, begin, end):
        regex_matches = self.re_compile.finditer(annotated_string.text, begin, end)
        indexes = list(map(lambda x: Annotation(self.name, x.start(), x.end()), regex_matches))
        return indexes
