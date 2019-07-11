# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


def two_teams(dict):
    first_team = []
    second_team = []
    for i, j in dict.items():
        if j > 40 or j < 20:
            first_team.append(i)
        else:
            second_team.append(i)
    print(sorted(first_team))
    print(sorted(second_team))
    return [sorted(first_team), sorted(second_team)]


if __name__ == '__main__':
    two_teams({
        'Smith': 34,
        'Wesson': 22,
        'Coleman': 45,
        'Abrahams': 19,
    }) == [
        ['Coleman', 'Abrahams'],
        ['Smith', 'Wesson']
    ]