from game import Person, bcolors
from magic import Spell
import random

#Black Magic
fireball = Spell("Fire", 20, 150, "black")
thunder = Spell("Thunder", 20, 140, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
quake = Spell("Quake", 30, 180, "black")
meteor = Spell("Meteor", 60, 400, "black")

#white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 20, 220, "white")

#People
player = Person(460, 100, 60, 34, [fireball,thunder,blizzard,meteor,cure,cura])
enemy = Person(1200, 65, 45, 25, [quake, thunder, cure])

#starting main game loop
running = True
i=0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
while running:
    print("=====================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.attack(enemy)
        print("You attacked for", dmg, "damage")
    elif index == 1:
        player.choose_magic(player.magic)
        magic_choice = int(input("Choose magic: ")) - 1
        player_spell = player.magic[magic_choice]
        dmg = player_spell.attack(player, enemy)
        if player_spell.type == "black":
            print(bcolors.OKBLUE + "\nYou hit them with", player_spell.name, "for", dmg, "dmg" + bcolors.ENDC)
        elif player_spell.type == "white":
            print(bcolors.OKBLUE + "\nYou healed yourself with", player_spell.name, "for", dmg, "hp" + bcolors.ENDC)
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
        break

    enemy_choice = random.randrange(0,2)
    if enemy_choice == 0:
        enemy_dmg = enemy.attack(player)
        print(bcolors.FAIL + "Enemy attacked for", enemy_dmg, "damage" + bcolors.ENDC)
    else:
        enemy_spell = enemy.magic[random.randrange(0,2)]
        if enemy_spell.cost > enemy.get_mp():
            enemy_dmg = enemy.attack(player)
            print(bcolors.FAIL + "Enemy attacked for", enemy_dmg, "damage" + bcolors.ENDC)
        else:
            dmg = enemy_spell.attack(enemy, player)
            if enemy_spell.type == "black":
                print(bcolors.FAIL + "\nThe enemy hit you with", enemy_spell.name, "for", dmg, "dmg" + bcolors.ENDC)
            elif enemy_spell.type == "white":
                print(bcolors.FAIL + "\nThe enemy healed themselves with", enemy_spell.name, "for", dmg, "hp" + bcolors.ENDC)

    print("=====================")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp())+ "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    print("Enemy MP:", bcolors.OKBLUE + str(enemy.get_mp()) + "/" + str(enemy.get_max_mp()) + bcolors.ENDC)
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp())+ "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    if player.get_hp() == 0:
        print(bcolors.FAIL + "You have been brutally murdered!" + bcolors.ENDC)
        running = False

