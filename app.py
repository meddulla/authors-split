#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from markov import MarkovChain


def save(filename, text):
    path = './split-discourses/'
    f = open(path + filename, 'a')
    f.write(text + '\n')
    f.close()


def main():
    text = ''
    base_path = './books/'
    authors_path = 'wittgenstein-carroll'
    files = [base_path + authors_path + '/lewis-carroll.txt',
             base_path + authors_path + '/wittgentstein.txt']

    for f in files:
        with open(f, 'r') as f:
            text += f.read()

    # special treatment for wittgenstein formulas
    text = re.sub(r'“(.+?)”', '', text)

    markov = MarkovChain(text=text)
    bipolar_discourse = markov.generate(100)
    print repr(bipolar_discourse)
    save(authors_path + '.txt', bipolar_discourse)


if __name__ == '__main__':
    main()
