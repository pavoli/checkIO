# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

"""
A pawn is generally a weak unit,
but we have 8 of them which we can use to build a pawn defense wall.
With this strategy, one pawn defends the others.
A pawn is safe if another pawn can capture a unit on that square.
We have several white pawns on the chess board and only white pawns.
You should design your code to find how many pawns are safe.
"""

#data = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
data = {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}

#print("c1" in data)
#print(str((chr(ord('d')-1)+str((2-1)))) in data or str((chr(ord('d')+1)+str((2-1)))) in data)
#print(str(chr(ord('d')-1)+str((2-1))))
#print(chr(ord('d')+1)+str((2-1)))

def safe_pawns(data):
    count = 0
    for i in data:
        letter, number = i[:1], int(i[1:])
        if (chr(ord(letter)-1)+str((number-1))) in data or (chr(ord(letter)+1)+str((number-1))) in data:
            count += 1
    return count

if __name__ == '__main__':
    print(safe_pawns(data))
    pass