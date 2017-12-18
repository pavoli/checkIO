# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

"""
This mission is the first one of the series.
Here you should find the length of the longest substring that consists of the same letter.
For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa".
The last substring is the longest one which makes it an answer.
Input: String.
Output: Int.
"""

#str = 'sdsffffse'
#str = 'ddvvrwwwrggg'
#str = ''
str = 'baababaab'

def long_repeat(str):
    if not len(str):
        return 0
    i=0
    count=1
    max_count=1
    while i<len(str)-1:
        if str[i] == str[i+1]:
            count += 1
            if count >= max_count:
                max_count = count
        else:
            count = 1
        i+=1
    return max_count

'''
from itertools import groupby

def long_repeat(line):
    return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)
'''

if __name__ == '__main__':
    print(long_repeat(str))