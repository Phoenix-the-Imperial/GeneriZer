"""
Copyright 2024 Rishav Chakraborty

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import numpy as np
import random
import spacy
from spacy.tokens import Doc
from spacy.matcher import Matcher
import json
from debug import Debug

random.seed(7)

dbg = Debug(0)

def get_weight(x: int) -> float:
    """
    The weight function for choosing elements from lists.

    Parameters
    ----------
    x: int
        The index of the element.
    
    Returns
    -------
    The weight corresponding to the element.
    """
    return 1 / x

def normalize_to_probabilities(weights: list |  np.ndarray) -> np.ndarray:
    """
    Given a list of weights, converts it to a list of probabilities bnby normalizing the sum to 1.
    """
    return np.array(weights) / np.sum(weights)

def get_probabilities(n: int) -> np.ndarray:
    """
    Returns the entire list of probabilities for an array of a given length n.
    """
    return normalize_to_probabilities([get_weight(x) for x in range(1, n + 1)])

def get_one_element_randomly(arr: list | np.ndarray):
    """
    Choose one element from the given list arr according to the weight function.
    """
    return np.random.choice(arr, 1, len(arr))[0]

def get_similar_words(word: str, n: int, include_original: bool = True) -> list:
    """
    Returns the n most similar words to the given word.

    Parameters
    ----------
    word: str
        The word of which the similar words are to be found.
    n: int
        The number of most similar words to return.
    include_original: bool, optional
        If the original word is to be included too. Default: True.

    Returns
    -------
    similar_words: list
        List of n most similar words to word including/excluding itself according to include_original.
    """
    word_hash: int = nlp.vocab.strings[word]
    similar_words = []
    ret = []
    if word_hash in nlp.vocab.vectors:
        similar_words = nlp.vocab.vectors.most_similar(np.array([nlp.vocab.vectors[word_hash]]), n = n)
        ret = [nlp.vocab.strings[similar_word].lower() for similar_word in similar_words[0][0] if (nlp.vocab.strings[similar_word] != word.lower())]
    if (include_original):
        ret = [word, *ret]
    return ret

def replace_synonyms(doc: Doc, n: int, max_k: int):
    """
    Returns the sentences with patterns replaced with vocubalry from a given corpus.

    Parameters
    ----------
    doc: Doc
        The document to operate on.
    n: int
        The number of similar words to consider.
    max_k: int
        The maximum length phrases to consider.

    Returns
    -------
    modified_doc: list
        The list of modified sentences according to the vocabulary from the corpus.
    """
    for sent in doc.sents:
        # TODO: Make it so that the already replaced phrases are ignored in the later runs.
        modified_sent = sent
        for k in range(1, max_k + 1):
            dbg.log(f'Length of the phrase: {k}')
            phrase_start = 0
            phrase_end = k
            while (phrase_end <= len(modified_sent)):
                phrase = modified_sent[phrase_start : phrase_end]
                dbg.log(f'Phrase: {phrase}')
                if (k == 1):
                    synonyms = get_similar_words(phrase.text, n)
                else:
                    synonyms = [phrase.text]
                dbg.log(f'Synonyms: {synonyms}')
                known_synonyms = [s for s in synonyms if s in replacement]
                if (len(known_synonyms) > 0):
                    synonym = str(get_one_element_randomly(known_synonyms))
                    dbg.log(f'Synonym: {synonym}')
                    if synonym in replacement:
                        if (type(replacement[synonym]) == str):
                            replacement_phrase = replacement[synonym]
                        elif (type(replacement[synonym]) == list):
                            replacement_phrase = str(get_one_element_randomly(replacement[synonym]))
                        else:
                            raise TypeError("Replacement word must be a string or a list of strings.")
                        dbg.log(f'replacement_phrase: {replacement_phrase}')
                        modified_sent = nlp.make_doc(modified_sent[ : phrase_start].text_with_ws + f'{replacement_phrase} ' + modified_sent[phrase_end : ].text_with_ws)
                        dbg.log(f'modified_sentence: {modified_sent}')
                        dbg.log(f'Add: {k - len(nlp.make_doc(replacement_phrase))}', 1)
                        phrase_start += k - len(nlp.make_doc(replacement_phrase))
                        phrase_end += k - len(nlp.make_doc(replacement_phrase))
                else:
                    phrase_start += 1
                    phrase_end += 1
        yield modified_sent

@spacy.Language.component("word_replacer")
def word_replacer(doc: Doc) -> Doc:
    """
    Replaces the phrases of a given document with the phrases replaced with the vocubulary from a given corpus.

    Parameters
    ----------
    doc: Doc
        The document to operate on.

    Returns
    -------
    modified_doc: spacy.language
        The document with the with the phrases replaced with the vocubulary from a given corpus.
    """
    if not Doc.has_extension('substitutes'):
        Doc.set_extension('substitutes', default = [])
    doc._.substitutes.extend(list(replace_synonyms(doc, 10, 2)))
    return doc

nlp = spacy.load("en_core_web_lg")
nlp.add_pipe('word_replacer')
matcher = Matcher(nlp.vocab)

with open('../data/wordmap.json', 'r') as f:
    replacement: dict = json.load(f)

patterns = [[{'LOWER': key}] for key in replacement]
matcher.add('TEST', patterns)

with open('../data/corpus.txt', 'r') as f:
    corpus = f.read().split('\n')

docs = nlp.pipe(corpus)
for doc in docs:
    print(doc.text)
    print(doc._.substitutes)
    print('***************************************************************')

dbg.write_log('../log/log.log')
