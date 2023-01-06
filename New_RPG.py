import random

player_health = 100
enemy_health = 100
critical_hit = 0
base_dmg = 1
sword = False
tf = [1, 0]
crit_multiplier = [2, 3, 4]
h_potion_inv = 0


sword = input("An enemy approaches, do you wish to draw your sword or fight with your fists? Type S for sword and F for fist: ") == "S"
if sword == True:
    base_dmg += 5

print("A battle commences!")

while player_health and enemy_health > 0:
    print(random.choice(["You attack", "It's your turn", "You go for the eyes"]))
    critical_hit = random.choice(tf)
    if critical_hit == 1:
        enemy_health -= (base_dmg * random.choice(crit_multiplier))
        if enemy_health < 0:
            enemy_health = 0
        print("You dealt a critical Hit! Enemy health is at", enemy_health)
    else:
        enemy_health -= base_dmg
        if enemy_health < 0:
            enemy_health = 0
        print("You've dealt", str(base_dmg), "damage leaving the enemy with", str(enemy_health), "health")

    if enemy_health > 0:
        print(random.choice(["The enemy attacks", "The attacker bites you", "Here comes the pain!"]))
        critical_hit = random.choice(tf)
        if critical_hit == 1:
            player_health -= (base_dmg * random.choice(crit_multiplier))
            if player_health < 0:
                player_health = 0
            print("You been hit with a critical Hit! Your health is at", player_health)
        else:
            player_health -= base_dmg
            if player_health < 0:
                player_health = 0
            print("The enemy dealt", str(base_dmg), "damage leaving you with", str(player_health), "health")

if player_health <= 0:
    print("You have died.")
if enemy_health <= 0:
    print("You have defeated the enemy!")

if player_health > 0:
    yes_potion = input("The enemy dropped 5 health potions would you like to pick them up? Y or N: ") == "Y"
    if yes_potion == True:
        h_potion_inv += 5
        yes_consume = input("Each potion heals you for 20 health. Would you like to consume one now? Y or N: ") == "Y"
        if yes_consume == True:
            player_health += 20
            print("You begrudgingly drink down the bad tasting potion, your health is now ", player_health)
        else:
            print("You decide to save them for later, your health remains at ", player_health)

    else:
        print("You are some kind of dumb huh?")

    if input("You look ahead and see that the path you are on diverges into 2 directions. Do you choose the Left or Right path? L or R: ") == "R":
        print("After contemplating the decision for awhile you decide embark down the right path")
        if input("Your health remains at " + str(player_health) + " Would you like to consume another potion? Y or N: ") == "Y":
            player_health += 20
            if player_health > 100:
                player_health = 100
            print("Your health has increased to ", player_health)
        else:
            print("You decide you are fine limping along on the brink of death and decide to horde your potions")
    else:
        print("You've gone left trying not to think too hard about if you have made the correct choice.")
        if input("Your health remains at " + str(player_health) + " Would you like to consume another potion? Y or N: ") == "Y":
            player_health += 20
            if player_health > 100:
                player_health = 100
            print("Your health has increased to ", player_health)
        else:
            print("You decide you are fine limping along on the brink of death and decide to horde your potions")