from classes.enemy import Enemy

enemy = Enemy(200, 60)
print("Health:", enemy.get_health())

import random

class Enemy:
    hp = 200
    def __init__(self, attack_low, attack_high):
        self.attack_low = attack_low
        self.attack_high = attack_high

    def getAttack(self):
        print("attack is", self.attack_low)

    def get_health(self):
        print("Health is", self.health)
enemy1 = Enemy(40, 49)
enemy1.getAttack()
enemy1.get_health()

enemy2 = Enemy(75, 90)
enemy2.getAttack()
enemy2.get_health()


player_health = 260 
enemyattack_low = 60
enemyattack_high = 80

while player_health > 0:
    damage = random.randrange(enemyattack_low, enemyattack_high)
    player_health = player_health - damage

    if player_health <= 30:
        player_health = 30

    print("enemy strikes for", damage, "points of damage. Current Health is", player_health)

    if player_health > 30: 
        continue

    if player_health == 0:
        print("You have died. You cannot respawn, as you are dead.")

    if player_health == 30:
        print("You have low health. You have been teleported to the nearest inn.")
        break