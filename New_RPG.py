import random
import time

player_health = 100
enemy_health = 100
critical_hit = 0
player_base_dmg = 3
enemy_base_dmg = 1
sword = False
tf = [1, 0]
crit_multiplier = [2, 3, 4]
h_potion_inv = 0


while True:
    player_health = 100
    enemy_health = 100
    dead_enemy = False

    # Global Commands:

    print("At anypoint during this game when you have the option to type. You can type \"Potion\" to consume a potion")
    time.sleep(1.00)
    while True:
        choice = input("An enemy approaches, do you wish to draw your sword or fight with your fists? Type S for sword and F for fist: ")
        if choice == "S":
            player_base_dmg += 5
            break
        if choice == "F":
            break
        if choice == "Potion" and h_potion_inv > 0:
            player_health += 20
            h_potion_inv -= 1
            print("You consume a health potion. Your health is at ", player_health)
        if choice == "Potion" and h_potion_inv <= 0:
            print("You are all out of potions")



    print("A battle commences!")

    while player_health > 0 and enemy_health > 0:
        time.sleep(0.25)
        print(random.choice(["You attack", "It's your turn", "You go for the eyes"]))
        critical_hit = random.choice(tf)
        if critical_hit == 1:
            enemy_health -= (player_base_dmg * random.choice(crit_multiplier))
            if enemy_health < 0:
                enemy_health = 0
            time.sleep(0.25)
            print("You dealt a critical Hit! Enemy health is at", enemy_health)
        else:
            enemy_health -= player_base_dmg
            if enemy_health < 0:
                enemy_health = 0
            time.sleep(0.25)
            print("You've dealt", str(player_base_dmg), "damage leaving the enemy with", str(enemy_health), "health")

        if enemy_health > 0:
            time.sleep(0.25)
            print(random.choice(["The enemy attacks", "The attacker bites you", "Here comes the pain!"]))
            critical_hit = random.choice(tf)
            if critical_hit == 1:
                player_health -= (enemy_base_dmg * random.choice(crit_multiplier))
                if player_health < 0:
                    player_health = 0
                time.sleep(0.25)
                print("You been hit with a critical Hit! Your health is at", player_health)
            else:
                player_health -= enemy_base_dmg
                if player_health < 0:
                    player_health = 0
                time.sleep(0.25)
                print("The enemy dealt", str(enemy_base_dmg), "damage leaving you with", str(player_health), "health")
        time.sleep(0.25)

        if player_health <= 0:
            print("You have died.")
            

        if enemy_health <= 0:
            dead_enemy = True
            print("You have defeated the enemy!")

    if dead_enemy == True:
        break
        
while True:
    choice = input("The enemy dropped 5 health potions would you like to pick them up? Y or N: ")
    if choice == "Y":
        h_potion_inv += 5
        break
    if choice == "N":
        print("You are some kind of dumb huh?")
        break
    if choice == "Potion" and h_potion_inv > 0:
        player_health += 20
        h_potion_inv -= 1
        if player_health > 100:
            player_health = 100
        print("You consume a health potion. Your health is at ", player_health)
    if choice == "Potion" and h_potion_inv <= 0:
        print("You are all out of potions")
while True:
    choice = input("Each potion heals you for 20 health. Would you like to consume one now? Y or N: ")
    if choice == "Y" and h_potion_inv > 0:
        player_health += 20
        if player_health > 100:
            player_health = 100
        h_potion_inv -= 1
        print("You begrudgingly drink down the bad tasting potion, your health is now ", player_health)
        print("You have " + str(h_potion_inv) + " health potions remaining")
        break
    if choice == "N":
        print("You decide to save them for later, your health remains at ", player_health)
        break
    if choice == "Potion" and h_potion_inv > 0:
        player_health += 20
        h_potion_inv -= 1
        if player_health > 100:
            player_health = 100
        print("You consume a health potion. Your health is at ", player_health)
        break
    if choice == "Potion" and h_potion_inv <= 0:
        print("You are all out of potions")
        break


    
while True:
    rl_choice = input("You look ahead and see that the path you are on diverges into 2 directions. Do you choose the Left or Right path? L or R: ")
    if rl_choice == "R":
        print("After contemplating the decision for awhile you decide embark down the right path")
        break
    if rl_choice == "L":
        print("You've gone left trying not to think too hard about if you have made the correct choice.")
        break
    if rl_choice == "Potion" and h_potion_inv > 0:
        player_health += 20
        h_potion_inv -= 1
        if player_health > 100:
            player_health = 100
        print("You consume a health potion. Your health is at ", player_health)
    if rl_choice == "Potion" and h_potion_inv <= 0:
        print("You are all out of potions")
while True:
    choice = input("Your health remains at " + str(player_health) + " Would you like to consume another potion? Y or N: ")
    if choice == "Y":
        player_health += 20
        h_potion_inv -= 1
        if player_health > 100:
            player_health = 100
        print("Your health has increased to ", player_health)
        break
    if choice == "N":
        if player_health < 30:
            print("You decide you are fine limping along on the brink of death and decide to horde your potions")
            break
        if player_health > 30 and player_health < 100:
            print("You decide to try and walk it off")
            break
        if player_health >= 100:
            print("Any othe choice would have been a waste of a potion")
            break
    if choice == "Potion" and h_potion_inv > 0:
        player_health += 20
        h_potion_inv -= 1
        if player_health > 100:
            player_health = 100
        print("You consume a health potion. Your health is at ", player_health)
        break
    if choice == "Potion" and h_potion_inv <= 0:
        print("You are all out of potions")
        break
    
    #if rl_choice == "R":