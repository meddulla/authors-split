#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import smtplib
from markov import MarkovChain


def send(msg):
    """Post to tumblr"""
    try:
        server = smtplib.SMTP_SSL()
        server.connect("smtp.gmail.com", 465)

        #Next, log in to the server
        server.login("email@gmail.com", "pass")

        #Send the mail
        msg = "\n" + msg  # The /n separates the message from the headers
        msg += "\n\n #wittgentstein-goes-bipolar-with-carroll"
        server.sendmail("email@gmail.com", "email@tumblr.com", msg)
        server.quit()
    except Exception, R:
        print R


def main():
    text = ''
    files = ['./books/wittgenstein-carroll/lewis-carroll.txt',
             './books/wittgenstein-carroll/wittgentstein.txt']

    for f in files:
        with open(f, 'r') as f:
            text += f.read()

    # special treatment for wittgenstein formulas
    text = re.sub(r'“(.+?)”', '', text)

    markov = MarkovChain(text=text)
    bipolar_discourse = markov.generate(100)
    print repr(bipolar_discourse)
    send(bipolar_discourse)

if __name__ == '__main__':
    main()
