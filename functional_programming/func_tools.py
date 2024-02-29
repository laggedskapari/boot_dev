import functools


def accumlate(doc, sentence):
    return doc + "." + sentence


def accumlate_first_sentences(sentences, n):
    return functools.reduce(accumlate, sentences[:n])
