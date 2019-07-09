# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


class Warrior():

    def __init__(self):
        self.health = 50
        self.attack = 5

    def is_alive(self):
        return True if self.health > 0 else False


class Knight(Warrior):

    def __init__(self):
        self.health = 50
        self.attack = 7


def fight(unit1, unit2):
    while unit1.health > 0 or unit2.health > 0:
        unit2.health -= unit1.attack
        unit1.health -= unit2.attack
    return True if unit1.health > 0 else False

if __name__ == '__main__':
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    print(fight(chuck, bruce))