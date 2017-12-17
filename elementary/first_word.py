# -*- coding: utf-8 -*-
import re

#s = 'Hello world'
#s = 'greetings, friends'
#s = ' a word '
#s = "don't touch it"
#s = "... and so on ..."
s = "Hello.World"


def first_word(str):
    new_str = str.replace(',', ' ')
    new_str = new_str.replace('.', ' ')
    for i in new_str.split(' '):
        if re.search('^([a-z]|[A-Z])+',i):
            return i



if __name__ == '__main__':
    print first_word(s)