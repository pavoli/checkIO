# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

'''
str = [
    "X.O",
    "XX.",
    "XOO"]
'''
'''
str = [
    "OO.",
    "XOX",
    "XOX"]
'''
'''
Tic-Tac-Toe, sometimes also known as Xs and Os,
is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid.
The player who succeeds in placing three respective marks in a horizontal,
vertical, or diagonal rows (NW-SE and NE-SW) wins the game
'''
str = [
    "OOX",
    "XXO",
    "OXX"]
''''''

def checkio(fields):
    #horizont
    for row in fields:
        if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]
    rotated_fields = zip(*fields)
    #vertical
    for row in rotated_fields:
        if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]
    #diagonal
    if (fields[0][0] == fields[1][1] == fields[2][2] or fields[0][2] == fields[1][1] == fields[2][0]) and fields[1][1] != '.':
        return fields[1][1]
    else:
        return 'D'

'''
def checkio(result):
    rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'
'''

if __name__ == '__main__':
    print(checkio(str))