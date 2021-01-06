import random
from game import bcolors
class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def attack(self, caster, enemy):
        mgl = self.dmg - 15
        mgh = self.dmg + 15
        cost = self.cost
        current_mp = caster.mp
        dmg = random.randrange(mgl,mgh)
        if cost > current_mp:
            print(bcolors.FAIL + "\nYou don't have enough mp" + bcolors.ENDC)
            return 0

        if self.type == "black":
            enemy.hp -= dmg
            if enemy.hp < 0:
                enemy.hp = 0
        elif self.type == "white":
            caster.hp += dmg
            if caster.get_hp() > caster.get_max_hp():
                caster.hp = caster.get_max_hp()

        caster.mp = current_mp - cost



        return dmg