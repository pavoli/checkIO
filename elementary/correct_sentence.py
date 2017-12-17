# -*- coding: utf-8 -*-

def correct_sentence(str):
    new_str = str[:]
    if not(new_str[0].isupper()):
        new_str = new_str[0].upper() + new_str[1:]
    if not(new_str[-1] == '.'):
        new_str += '.'
    return new_str


if __name__ == '__main__':
    print correct_sentence('greetings, friends')