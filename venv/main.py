from game import Person, bcolors

magic = [{"name": "Fireball", "cost" : 10, "dmg": 60},
         {"name": "Thunder", "cost" : 20, "dmg": 75},
         {"name": "Blizzard", "cost" : 30, "dmg": 100}]
player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

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
        player.choose_magic(magic)
        magic_choice = int(input("Choose magic: ")) - 1
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_cost(magic_choice)
        current_mp = player.get_mp()
        if cost > current_mp:
            print(bcolors.FAIL + "\nYou don't have enough mp" + bcolors.ENDC)
            continue

        player.reduce_mp(cost);
        dmg = player.attack_spell(magic_choice, enemy)
        print(bcolors.OKBLUE + "\nYou hit them with", spell, "for", dmg, "dmg" + bcolors.ENDC)


    enemy_choice = 1
    enemy_dmg = enemy.attack(player)
    print("Enemy attacked for", enemy_dmg, "damage")
    print("=====================")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp())+ "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp())+ "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You have been brutally murdered!" + bcolors.ENDC)
        running = False

