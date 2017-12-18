# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

"""
You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.
"""

import string

#("Hello World!") == "l"
#("How do you do?") == "o"
#("One") == "e"
#("Oops!") == "o"
#("AAaooo!!!!") == "a"
#("abe") == "a"

#print(ord('o'))
#print(ord('n'))
#print(ord('e'))
#print(ord('a'))

#for i in range(ord('a'), ord('z')+1):
#    print(i, end=' ')

#str = 'Hello World!'
#str = 'How do you do?'
#str = 'One'
#str = 'Oops!'
#str = 'AAaooo!!!!!'
#str = 'abe'
str = 'Lorem ipsum dolor sit amet'

''''''
def checkio(str):
    new_str = [i for i in str.lower() if ord(i) in range(ord('a'), ord('z')+1)]
    result = new_str[0]
    min_ord_letter = ord(result)
    max_count = new_str.count(result)
    del new_str[0]
    for i in new_str:
        if new_str.count(i) > max_count:
            result = i
            max_count = new_str.count(i)
            min_ord_letter = ord(i)
        elif new_str.count(i) == max_count:
            if ord(i) < min_ord_letter:
                result = i
                min_ord_letter = ord(i)
    return result
''''''

'''
def checkio(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)
'''


if __name__ == '__main__':
    print(checkio(str))