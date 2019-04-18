# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def easy_unpack(in_tuple):
    #new_list = list(in_tuple)
    #return (new_list[0], new_list[2], new_list[-2])
    return (in_tuple[0], in_tuple[2], in_tuple[-2])
    #return tuple([elements[x] for x in (0, 2, -2)])


if __name__ == '__main__':
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7))
    print(easy_unpack((1, 1, 1, 1)) == (1, 1, 1))
    print(easy_unpack((6, 3, 7)) == (6, 7, 3))