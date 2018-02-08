from AnnotatedString import AnnotatedString
from ListAnnotationIndex import ListAnnotationIndex
from NGramAnnotator import NGramAnnotator
from RegexAnnotator import RegexAnnotator


def main():
    s = AnnotatedString("Alan W Black is a Scottish computer scientist, known for his research on speech synthesis. He is a professor in the Language Technology Institute at Carnegie Mellon University in Pittsburgh, Pennsylvania.",
                        ListAnnotationIndex())
    a1 = RegexAnnotator("Sentence", r'\b[^\.]+\b')
    a1.process(s)
    a2 = RegexAnnotator("Token", r'\w+')
    a3 = NGramAnnotator(2, "Token", "TokenBigram")

    for sentence in s.index.get_annotations("Sentence"):
        print(str(sentence) + " " + s.text[sentence.begin:sentence.end])
        a2.process(s, sentence.begin, sentence.end)
        a3.process(s, sentence.begin, sentence.end)
        for token in s.index.get_annotations("Token", sentence.begin, sentence.end):
            print(str(token) + " " + s.text[token.begin:token.end])
        for ngram in s.index.get_annotations("TokenBigram", sentence.begin, sentence.end):
            print(str(ngram) + " " + s.text[ngram.begin:ngram.end])


if __name__ == "__main__":
    main()
