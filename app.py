#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
from markov import MarkovChain


def save(filename, text):
    path = './split-discourses/'
    f = open(path + filename, 'a')
    f.write('\n.\n' + text + '\n\n')
    f.close()


def run_dir(base_path, authors_path):
    text = ''
    path = base_path + authors_path + '/'
    files = [name for name in os.listdir(path) if '.txt' in name]

    for f in files:
        with open(path + f, 'r') as f:
            text += f.read()

    # special treatment for wittgenstein formulas
    text = re.sub(r'“(.+?)”', '', text)

    markov = MarkovChain(text=text)
    bipolar_discourse = markov.generate(100)
    print repr(bipolar_discourse)
    save(authors_path + '.txt', bipolar_discourse)


def main():
    base_path = './books/'
    for name in os.listdir(base_path):
        if os.path.isdir(os.path.join(base_path, name)):
            run_dir(base_path, name)


if __name__ == '__main__':
    main()
