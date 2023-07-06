from classes.game import Person, bcolours
from classes.magic import Spell
from classes.inventory import Item
import random

'''
Hp/hp/self_hp = Player heath points
MP/mp = Player magic points
Max_hp = Maximum health points
player.reduce_mp = Reduce magic points from player
player.max_hp = Player maxium health points
self.max_mp = Player maxiumum magic points
hp_bar = hit points bar
bar_ticks = bar score
mp_bar = magic points bar
current_hp = current health points
current_mp = current magic points 
current_hp = current health points
del = delete

'''

#Black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

#White magic
cure = Spell("cure", 12, 120, "white")
cura = Spell("cura", 18, 200, "white")
curaga = Spell("Curaga", 50, 6000, "white")

potion = Item("Potion", "potion", "Heals 50 Hp", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 Hp", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 Hp", 500)
elixer = Item("Elixer", "elixer", "Fully restores Hp/Mp of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's Hp/Mp", 9999)

grenade = Item("Grenade", "attack", "deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [fire, meteor, curaga]
player_items = [
    {"item": potion, "quantity": 15}, 
    {"item": hipotion, "quantity": 5},
    {"item": superpotion, "quantity": 5},
    {"item": elixer, "quantity": 5}, 
    {"item": hielixer, "quantity": 2},
    {"item": grenade, "quantity": 5}]

player1 = Person("Spiderman      ", 3260, 132, 60, 34, player_spells, player_items)
player2 = Person("Batman         ", 4160, 188, 60, 34, player_spells, player_items)
player3 = Person("Optimum Prime  ", 3089, 174, 60, 34, player_spells, player_items)

enemy1 = Person("Voldermort      ", 1250, 130, 560, 325, enemy_spells, [])
enemy2 = Person("Valos           ", 1200, 221, 45, 25, enemy_spells, [])
enemy3 = Person("Darth Vader     ", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3 ]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(bcolours.FAIL + bcolours.BOLD + "AN ENEMY ATTACKS!" + bcolours.ENDC)

def attack(player):
    damage = player.generate_damage()
    enemy_index = player.choose_target(enemies)
            
    enemies[enemy_index].take_damage(damage)
    print("You attacked for " + enemies[enemy_index].name + " for ", damage, 
        "points of damage. Enemy Hp: ", enemy.hp)

    if enemies[enemy_index].get_hp() == 0:
        print(enemies[enemy_index].name.replace(" ", "") + " has died. ")
        del enemies[enemy_index]

def magic(player):
    player.choose_magic()
    print("\n")
    magic_choice = int(input("    Choose magic: ")) - 1

    if magic_choice == - 1:
        return

    spell = player.magic[magic_choice]
    magic_damage = spell.generate_damage()

    current_magic_points = player.mp

    if spell.cost > current_magic_points:
        print(bcolours.FAIL + "\nNot enough Mp\n" + bcolours.ENDC)
        return

    player.reduce_mp(spell.cost)

    if spell.type == "white":
        player.heal(magic_damage)
        print(bcolours.OKBLUE + spell.name + " heals "+ player.name + " for", str(magic_damage), "Hp." + bcolours.ENDC)

    elif spell.type == "black":
            target = random.randrange(0, len(enemies))
            enemy = enemies[target]
            enemy.take_damage(magic_damage)
            print(bcolours.OKBLUE + "\n" + player.name.replace(" ","") + "'s " + spell.name + " deals ", str(magic_damage), 
            "points of damage " + enemy.name + bcolours.ENDC)

            if enemies[target].get_hp() == 0:
                print(enemies[target].name.replace(" ", "") + " has died. ")
                del enemies[target]

def item(player):
    player.choose_item()
    print("\n")
    item_choice = int(input("    Choose item: ")) - 1

    if item_choice == - 1:
        return

    item = player.items[item_choice]["item"]

    if player.items[item_choice]["quantity"] == 0:
        print(bcolours.FAIL + "\n" + "None left..." + bcolours.ENDC)
        return

    player.items[item_choice]["quantity"] -= 1
        
    if item.type == "potion":
        player.heal(item.prop)
        print(bcolours.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "Hp" + bcolours.ENDC)

    elif item.type == "elixer":
        if item.name == "MegaElixer":
            for i in players:
                    i.hp = i.max_hp
                    i.mp = i.max_mp

            else:
                    player.hp = player.max_hp
                    player.mp = player.max_mp
            
            print(bcolours.OKGREEN + "\n" + item.name + " Fully restores Hp/Mp " + bcolours.ENDC)
        
    elif item.type == "attack":
        enemy_index = player.choose_target(enemies)

        enemies[enemy_index].take_damage(item.prop)
        print(bcolours.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to " + enemies[enemy_index].name + bcolours.ENDC)

        if enemies[enemy_index].get_hp() == 0:
            print(enemies[enemy_index].name.replace(" ", "") + " has died. ")
            del enemies[enemy_index]
        # print ("Enemy chose", spell, "damage is", magic_damage)

while running: 
    print("===================")

    print("\n\n")
    print("NAME                      HP                                           MP")
    for player in players:
        player.get_stats()
       
    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        
        player.choose_action()
        choice = input("    Choose action: ")

        index = int(choice) - 1

        if index == 0:
            attack(player)
                
        elif index == 1:
            magic(player)

        elif index == 2:
            item(player)

    # Check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1
    
    for player in players:
        if player.get_hp() == 0:
            player += 1
    
    # Check if player won
    if defeated_enemies == 2:
        print(bcolours.OKGREEN + "You win!" + bcolours.ENDC)
        running = False

    # Check if enemy won
    elif defeated_players == len(players):
        print(bcolours.FAIL + "Your enemies have defeated you!" + bcolours.ENDC)
        running = False

    print("\n")
    # Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            # Chose attack
            target = random.randrange(0, 3)
            enemy_damage = enemies[0].generate_damage()

            players[target].take_damage(enemy_damage)
            print(enemy.name.replace(" ", "") + " attacks " + 
                players[target].name.replace(" ", "") + " for", enemy_damage)
        
        elif enemy_choice == 1:
           spell = enemy.choose_enemy_spell()
           magic_damage = spell.generate_damage()
           enemy.reduce_mp(spell.cost)
           print("Enemy chose", spell.name, "damage is", magic_damage)

