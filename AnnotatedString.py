

class AnnotatedString:

    def __init__(self, text, index):
        self.text = text
        self.index = index

    def hard_match(self, a2, annotation_type):
        a1_list = self.index.get_annotations(annotation_type)
        a2_list = a2.index.get_annotations(annotation_type)
        for a1 in a1_list:
            if not any(self._compare_annotation(self.text, a1, a2.text, a2) for a2 in a2_list):
                return False
        return True

    def soft_match(self, a2, annotation_type):
        match_count = 0
        a1_list = self.index.get_annotations(annotation_type)
        a2_list = a2.index.get_annotations(annotation_type)
        for annotation_a1 in a1_list:
            if any(self._compare_annotation(self.text, annotation_a1, a2.text, annotation_a2) for annotation_a2 in a2_list):
                match_count += 1
        if len(a1_list) > 0:
            return float(match_count)/len(a1_list)
        else:
            return 0

    @staticmethod
    def _compare_annotation(str1, a1, str2, a2):
        return str1[a1.begin : a1.end] == str2[a2.begin : a2.end]
