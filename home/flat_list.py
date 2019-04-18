# -*- coding: utf-8 -*-
#! /usr/local/bin/python3
__author__ = 'p.olifer'


def flat_list(array):
    new_list = []
    def work_list(lst):
        for x in lst:
            if type(x) is not list:
                new_list.append(x)
            else:
                work_list(x)
        return (new_list)
    work_list(array)
    return new_list

if __name__ == '__main__':
    #print(flat_list([1, 2, 3]) == [1, 2, 3])
    print(flat_list([1, 2, 3]))
    #print(flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4])
    print(flat_list([1, [2, 2, 2], 4]))
    #print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7])
    print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
    #print(flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1])
    print(flat_list([-1, [1, [-2], 1], -1]))