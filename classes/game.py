import random

class bcolours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, attack, defense, magic, items):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attack_low = attack - 10
        self.attack_high = attack + 10
        self.defense = defense
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_high)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
            return self.hp
        
    def heal(self, damage):
        self.hp += damage 
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost
    
    def  choose_action(self):
        i = 1
        print("\n" + "      " + bcolours.BOLD + self.name + bcolours.ENDC)
        print(bcolours.OKBLUE + bcolours.BOLD + "       ACTIONS:" + bcolours.ENDC)
        for item in self.actions:
            print("       " +str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolours.OKBLUE + bcolours.BOLD + "      MAGIC:" + bcolours.ENDC)
        for spell in self.magic:
            print("       " +str(i) + ".", spell.name, "(cost:)", str(spell.cost) + ")")
            i += 1
    
    def choose_item(self):
        i = 1
        print("\n" + bcolours.OKGREEN + bcolours.BOLD + "     ITEMS:" + bcolours.ENDC)
        for item in self.items:
            print ("     " + str(i) + ".", item["item"].name + ":", item["item"].description,
                 " (x" + str(item["quantity"])+")")
            i += 1

    def choose_target(self, enemies):
        i = 1

        print("\n" + bcolours.FAIL + bcolours.BOLD + "    Target:" + bcolours.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose target: ")) -1
        return choice

            
    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp/self.max_hp) * 100 /2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += ""

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased < 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                            __________________________________________________")
        print(bcolours.BOLD + self.name + " " + 
            current_hp +" |" + bcolours.FAIL + hp_bar + bcolours.ENDC + "|" )

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.max_hp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.max_mp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while bar_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while bar_ticks > 10:
          mp_bar += ""

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased < 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.max_mp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += ""
                decreased += 1
            current_mp += mp_string

        else: 
            current_mp = mp_string

        print("                               _________________________         _____________")
        print(bcolours.BOLD + self.name + "     " + 
            current_hp +" |" + bcolours.OKGREEN + hp_bar + bcolours.ENDC + "|        " + 
            current_mp + "/" + str(self.max_mp) + " |" + bcolours.OKBLUE + mp_bar + bcolours.ENDC + "|" )

    def choose_enemy_spell(self):
        if self.get_hp() < 0.3 * self.get_max_hp():
            magic_choice = random.randrange(5, 7)
            spell = self.magic[magic_choice]
            if self.get_mp() > spell.cost:
                self.reduce_mp(spell.cost)
            else:
                return
        else:
            magic_choice = random.randrange(0, len(self.magic))
            spell = self.magic[magic_choice]
            if self.get_mp() > spell.cost:
                self.reduce_mp(spell.cost)
            else:
                return
        return spell