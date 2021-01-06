import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        # pick random number in range for atks
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def attack(self, enemy):
        dmg = random.randrange(self.atkl, self.atkh)
        enemy.hp -= dmg
        if enemy.get_hp() < 0:
            enemy.hp = 0
        return dmg




    #Generating getters for ease of use later
    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    # iterate through actions and print them for user
    def choose_action(self):
        i = 1
        print("Actions:")
        for item in self.actions:
            print(str(i) + " : ", item)
            i+= 1

    # iterate through magic choices along with cost and print them for user
    def choose_magic(self, spell):
        i = 1
        print("Magic:")
        for item in spell:
            print(str(i) + " : ", item.name, "(cost : ", str(item.cost) + ")")
            i += 1