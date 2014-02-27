#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import re

DEFAULT_TOKEN_PATTERN = ur"\b[a-zA-z'][a-zA-z']*\b"


class MarkovChain(object):

    def __init__(self, open_file=None, text=None):
        self.cache = {}
        if open_file is None and text is None:
            raise Exception("No file or word list sent to the '\
                constructor of the markov chain")
        if open_file:
            self.open_file = open_file
            self.words = self._file_to_words(open_file)
        else:
            self.words = self._tokenize(text)

        self.word_size = len(self.words)
        self._cache()

    def _tokenize(self, text):
        compiled = re.compile(DEFAULT_TOKEN_PATTERN, re.UNICODE)
        tokens = compiled.findall(text)
        return [w.lower() for w in tokens]

    def _file_to_words(self):
        self.open_file_seek(0)
        data = self.open_file.read()
        words = self._tokenize(data)
        return words

    def _triples(self):
        if len(self.words) < 3:
            return

        for i in range(len(self.words) - 2):
            yield (self.words[i], self.words[i+1], self.words[i+2])

    def _cache(self):
        for w1, w2, w3 in self._triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]

    def generate(self, size=25):
        seed = random.randint(0, self.word_size-3)
        w1, w2 = self.words[seed], self.words[seed+1]
        gen_words = []
        for i in xrange(size):
            if (w1, w2) in self.cache:
                gen_words.append(w1)
                w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        gen_words.append(w2)
        return ' '.join(gen_words)

if __name__ == '__main__':
    text = """4.2211  he could have shouted and could not. He spoke little,
    and then almost huskily, with the
    low-voiced timidity of a man who shrinks
    from argument. he doesn't want to """
    chain = MarkovChain(text=text)
    print repr(chain.generate())
