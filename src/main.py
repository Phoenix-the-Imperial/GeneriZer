import numpy as np
import spacy
from spacy.tokens import Doc
from spacy.matcher import Matcher
import json

def get_similar_words(word: str, n: int, include_original: bool = True) -> list:
    word_hash: int = nlp.vocab.strings[word]
    similar_words = []
    ret = []
    if word_hash in nlp.vocab.vectors:
        similar_words = nlp.vocab.vectors.most_similar(np.array([nlp.vocab.vectors[word_hash]]), n = n)
        # ret = [nlp.vocab.strings[similar_word].lower() for similar_word in similar_words[0][0] if (include_original or nlp.vocab.strings[similar_word] != word.lower())]
        ret = [nlp.vocab.strings[similar_word].lower() for similar_word in similar_words[0][0] if (nlp.vocab.strings[similar_word] != word.lower())]
    if (include_original):
        ret = [word, *ret]
    return ret

# def replace_synonyms(doc: spacy.Language, n: int):
#     for sent in doc.sents:
#         matches = matcher(sent)
#         for _, start, end in matches:
#             print(f'Start: {start}, End: {end}')
#             span = sent[start : end]
#             synonyms = get_similar_words(span.text, n)
#             for synonym in synonyms:
#                 yield nlp.make_doc(sent[ : start].text_with_ws + f'{synonym} ' + sent[end : ].text_with_ws)

# @spacy.Language.component("synonym_replacer")
# def synonym_replacer(doc):
#     if not Doc.has_extension('synonyms'):
#         Doc.set_extension('synonyms', default=[])
#     doc._.synonyms.extend(list(replace_synonyms(doc, 4)))
#     return doc

# def replace_synonyms(doc: spacy.Language, n: int):
#     for sent in doc.sents:
#         print(f'Sentence: {sent.text}')
#         matches = matcher(sent)
#         print(f'Matches: {matches}')
#         for _, start, end in matches:
#             print(nlp.vocab.strings[_])
#             print(f'Start: {start}, End: {end}')
#             span = sent[start : end]
#             synonyms = get_similar_words(span.text, n)
#             print(f'Synonyms: {synonyms}')
#             for synonym in synonyms:
#                 if synonym in replacement:
#                     if (type(replacement[synonym]) == str):
#                         print(f'Replacement type is a list.')
#                         yield nlp.make_doc(sent[ : start].text_with_ws + f'{replacement[synonym]} ' + sent[end : ].text_with_ws)
#                     elif (type(replacement[synonym]) == list):
#                         print(f'Replacement type is a list.')
#                         yield nlp.make_doc(sent[ : start].text_with_ws + f'{replacement[synonym][0]} ' + sent[end : ].text_with_ws)
#                     else:
#                         print(f'Replacement type is neither.')
#                         raise TypeError("Replacement word must be a string or a list of strings.")

def replace_synonyms(doc: spacy.Language, n: int):
    for sent in doc.sents:
        # print(f'Sentence: {sent.text}')
        matches = matcher(sent)
        # print(f'Matches: {matches}')
        for _, start, end in matches:
            # print(nlp.vocab.strings[_])
            print(f'Start: {start}, End: {end}')
            span = sent[start : end]
            if (start + 1 == end):
                synonyms = get_similar_words(span.text, n)
            else:
                synonyms = [span.text]
            print(f'Synonyms: {synonyms}')
            for synonym in synonyms:
                if synonym in replacement:
                    # print(f'Key exists!')
                    if (type(replacement[synonym]) == str):
                        # print(f'Replacement type is a list.')
                        yield nlp.make_doc(sent[ : start].text_with_ws + f'{replacement[synonym]} ' + sent[end : ].text_with_ws)
                    elif (type(replacement[synonym]) == list):
                        # print(f'Replacement type is a list.')
                        yield nlp.make_doc(sent[ : start].text_with_ws + f'{replacement[synonym][0]} ' + sent[end : ].text_with_ws)
                    else:
                        raise TypeError("Replacement word must be a string or a list of strings.")

@spacy.Language.component("word_replacer")
def word_replacer(doc):
    if not Doc.has_extension('substitutes'):
        Doc.set_extension('substitutes', default = [])
    doc._.substitutes.extend(list(replace_synonyms(doc, 10)))
    return doc

# print(get_similar_words("good", 100))

nlp = spacy.load("en_core_web_lg")
nlp.add_pipe('word_replacer')
matcher = Matcher(nlp.vocab)
# patterns = [[{'LOWER': 'good'}], [{'LOWER': 'great'}]]

# replacement = dict({
#     'fantastic': 'bussin',
#     'terrific': 'lit'
# })
with open('../data/wordmap.json', 'r') as f:
    replacement = json.load(f)
print(replacement['as fuck'])
print(replacement)

patterns = [[{'LOWER': key}] for key in replacement]
print(f'patterns: {patterns}')
matcher.add('TEST', patterns)

# corpus = ['I have a great dog', 'Hi this is my dog']
corpus = [
    'This is a great pen',
    'You are a very good boy',
    'This is boring as fuck',
    'I do not like your vibe'
]
docs = nlp.pipe(corpus)
for doc in docs:
    print(doc.text)
    print(doc._.substitutes)
    print('**********************************************')