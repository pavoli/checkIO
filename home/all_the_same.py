# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def all_the_same(input_list):
    if len(input_list) == 0:
        return True
    a, *b = input_list
    count = 1
    for x in b:
        if x == a:
            count += 1
    if count == len(input_list):
        return True
    else:
        return False
    #return True if len(set(elements)) < 2 else False
    #return len(set(elements)) < 2


if __name__ == '__main__':
    #print(all_the_same([1, 1, 1])) == True
    print(all_the_same([1, 1, 1]))
    #all_the_same([1, 2, 1]) == False
    print(all_the_same([1, 2, 1]))
    #all_the_same(['a', 'a', 'a']) == True
    print(all_the_same(['a', 'a', 'a']))
    #all_the_same([]) == True
    print(all_the_same([]))