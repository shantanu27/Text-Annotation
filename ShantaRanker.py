from IndependentRanker import IndependentRanker

from text_annotation.AnnotatedString import AnnotatedString
from text_annotation.annotation_index.ListAnnotationIndex import ListAnnotationIndex
from text_annotation.annotator import NGramAnnotator as ng
from text_annotation.annotator import RegexAnnotator as reg


class ShantaRanker(IndependentRanker):

    def rankAnswer(self, question, answer):

        question_as = AnnotatedString(question, ListAnnotationIndex())
        answer_as = AnnotatedString(answer, ListAnnotationIndex())
        a1 = reg.RegexAnnotator("Sentence", r'\b[^\.]+\b')
        a1.process(question_as)
        a1.process(answer_as)
        a2 = reg.RegexAnnotator("Token", r'\w+')
        a3 = ng.NGramAnnotator(2, "Token", "TokenBigram")

        for q_sentence in question_as.index.get_annotations("Sentence"):
            #print(str(sentence) + " " + question_as.text[sentence.begin:sentence.end])
            a2.process(question_as, q_sentence.begin, q_sentence.end)
            a3.process(question_as, q_sentence.begin, q_sentence.end)
            # for token in question_as.index.get_annotations("Token", sentence.begin, sentence.end):
            #     print(str(token) + " " + question_as.text[token.begin:token.end])
            # for ngram in question_as.index.get_annotations("TokenBigram", sentence.begin, sentence.end):
            #     print(str(ngram) + " " + question_as.text[ngram.begin:ngram.end])

        for a_sentence in answer_as.index.get_annotations("Sentence"):
            a2.process(answer_as, a_sentence.begin, a_sentence.end)
            a3.process(answer_as, a_sentence.begin, a_sentence.end)

        return question_as.soft_match(answer_as, "TokenBigram")

    def getName(self):
        return "ShantaRanker"



