# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

"""
The function should recognise if a subject line is stressful.
A stressful subject line means that all letters are uppercase,
and/or ends by at least 3 exclamation marks and/or contains
at least one of the following “red” words "help", "asap", "urgent".
Any of those "red" words can be spelled in different ways -
"HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP"
Input: Subject line as a string
Output: Boolean.
"""

#str = 'Hi'
#str = 'I need HELP'
str = 'h!e!l!p'

STRESS_WORDS = ('!!!', 'help', 'asap', 'urgent')

def is_stressfull(str):
    new_str = [i for i in str.lower() if i.isalpha()]
    print(new_str)
    ans = 0
    for i in STRESS_WORDS:
        print('i=', i, '| new_str=', new_str)
        if i in new_str:
            ans = 1
            break
    if ans == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_stressfull(str))