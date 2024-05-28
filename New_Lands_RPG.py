# import python libraries
import math
import os
import pickle
import random
import secrets
import sys
import time

# People
PLAYER = 10
BANDIT = 10

# first starting area
Wood = random.randint(0, 10)
Stone = random.randint(0, 10)
Iron = random.randint(0, 10)
Gold = random.randint(0, 1)
Copper = random.randint(0, 10)
Fish = random.randint(0, 10)

# world
DISTANCE = random.randint(5, 10)

# inventory
IWOOD = 0
ISTONE = 0
IIRON = 0
IGOLD = 0
ICOPPER = 0
IFISH = 0

# bank
BWOOD = 0
BSTONE = 0
BIRON = 0
BGOLD = 0
BCOPPER = 0
BFISH = 0

# Xp system
Xp = 0
Level = 1
XpLEFT = 100


print("========================================")
print("Type 'help' for help")

while True:  # start of game
    print("========================================")
    Choose_action = input("choose action: ").lower()

    match Choose_action:  # Choose your action

        case "scan":  # scan area for resources
            print("========================================")
            print("Resource list")
            print("----------------------------------------")
            print("Wood", Wood, "\nStone", Stone, "\nIron",
                  Iron, "\nGold", Gold, "\nCopper", Copper,
                  "\nFish", Fish, )

        case "mine":  # select collection mode
            while True:
                mine = input("choose resource: ")
                match mine:
                    case "all wood":
                        while True:
                            if Wood >= 1:
                                time.sleep(1)
                                print("you collected +1 wood")
                                Wood -= 1
                                IWOOD += 1
                                Xp += 10
                                XpLEFT -= 10
                            else:
                                print("there is no more resource to collect")
                                break

                    case "all stone":
                        while True:
                            if Stone >= 1:
                                time.sleep(1)
                                print("you collected +1 stone")
                                Stone -= 1
                                ISTONE += 1
                                Xp += 10
                                XpLEFT -= 10
                            else:
                                print("there is no more resource to collect")
                                break

                    case "all iron":
                        while True:
                            if Iron >= 1:
                                time.sleep(1)
                                print("you collected +1 iron")
                                Iron -= 1
                                IIRON += 1
                                Xp += 10
                                XpLEFT -= 10
                            else:
                                print("there is no more resource to collect")
                                break

                    case "all gold":
                        while True:
                            if Gold >= 1:
                                time.sleep(1)
                                print("you collected +1 gold")
                                Gold -= 1
                                IGOLD += 1
                                Xp += 10
                                XpLEFT -= 10
                            else:
                                print("there is no more resource to collect")
                                break

                    case "all copper":
                        while True:
                            if Copper >= 1:
                                time.sleep(1)
                                print("you collected +1 copper")
                                Copper -= 1
                                ICOPPER += 1
                                Xp += 10
                                XpLEFT -= 10
                            else:
                                print("there is no more resource to collect")
                                break

                    case "all fish":
                        while True:
                            if Fish >= 1:
                                time.sleep(1)
                                print("you collected +1 fish")
                                Fish -= 1
                                IFISH += 1
                                Xp += 10
                                XpLEFT -= 10
                            else:
                                print("there is no more resource to collect")
                                break

                    case "wood":
                        if Wood >= 1:
                            print("you collected +1 wood")
                            Wood -= 1
                            IWOOD += 1
                            Xp += 10
                            XpLEFT -= 10
                        else:
                            print("there is no more resource to collect")

                    case "stone":
                        if Stone >= 1:
                            print("you collected +1 stone")
                            Stone -= 1
                            ISTONE += 1
                            Xp += 10
                            XpLEFT -= 10
                        else:
                            print("there is no more resource to collect")

                    case "iron":
                        if Iron >= 1:
                            print("you collected +1 iron")
                            Iron -= 1
                            IIRON += 1
                            Xp += 10
                            XpLEFT -= 10
                        else:
                            print("there is no more resource to collect")

                    case "gold":
                        if Gold >= 1:
                            print("you collected +1 gold")
                            Gold -= 1
                            IGOLD += 1
                            Xp += 10
                            XpLEFT -= 10
                        else:
                            print("there is no more resource to collect")

                    case "copper":
                        if Copper >= 1:
                            print("you collected +1 copper")
                            Copper -= 1
                            ICOPPER += 1
                            Xp += 10
                            XpLEFT -= 10
                        else:
                            print("there is no more resource to collect")

                    case "fish":
                        if Fish >= 1:
                            print("you collected +1 Fish")
                            Fish -= 1
                            IFISH += 1
                            Xp += 10
                            XpLEFT -= 10
                        else:
                            print("there is no more resource to collect")

                    case "scan":  # scan area for resources
                        print("========================================")
                        print("Resource list:")
                        print("----------------------------------------")
                        print("Wood", Wood, "\nStone", Stone, "\nIron",
                              Iron, "\nGold", Gold, "\nCopper", Copper,
                              "\nFish", Fish, )

                    case "bag":  # check inventory
                        print("========================================")
                        print("Inventory")
                        print("----------------------------------------")
                        print("Wood", IWOOD, "\nStone", ISTONE, "\nIron", IIRON, "\nGold", IGOLD,
                              "\nCopper", ICOPPER, "\nFish", IFISH)
                        print("----------------------------------------")

                    case "help":
                        print("========================================")
                        print("Mining mode help menu:")
                        print("----------------------------------------")
                        print("Type the name of the resource you desire to collect\nActions:\n"
                              "Scan - Scans area for resources\nStop - leaves mining mode\nAll - Type (all) followed by"
                              " the name of the resource\nto automatically collect resources\n"
                              "Note: There is a 1 second delay between auto collect.")
                        print("========================================")
                    case "stop":
                        print("you stop mining")
                        break

                    case _:
                        print("Invalid action ")

    # xp system and leveling up calculations
    if Level >= 80:
        if XpLEFT <= 1:
            Level += 1
            XpCALC = Level * 1000
            XpLEFT += XpCALC
    else:
        if Level >= 49:
            if XpLEFT >= 1:
                Level += 1
                XpCALC = Level * 500
                XpLEFT += XpCALC
        else:
            if Level >= 0:
                if XpLEFT <= 1:
                    Level += 1
                    XpCALC = Level * 100 + 100
                    XpLEFT += XpCALC

    match Choose_action:  # continuation of choose you action
        case "bag":  # check inventory
            print("========================================")
            print("Inventory:")
            print("----------------------------------------")
            print("Wood", IWOOD, "\nStone", ISTONE, "\nIron", IIRON, "\nGold", IGOLD, "\nCopper", ICOPPER, "\nFish",
                  IFISH)
            print("----------------------------------------")

        case "help":  # prints list of available commands
            print("========================================")
            print("actions list:")
            print("scan, travel, mine, bag, level")

        case "level":  # check level
            print("Total Xp earned", Xp)
            print("current level", Level)
            print("needed Xp to next level:", XpLEFT)

        case "lvl":  # check level
            print("Total Xp earned", Xp)
            print("current level", Level)
            print("needed Xp to next level:", XpLEFT)

        case "travel":  # travel to different section
            TRAVELTIME = random.randint(7, 15)
            print("7-15 seconds until you arrive at new area")
            time.sleep(TRAVELTIME)
            RANDOM = random.randint(0, 1)

            if RANDOM == 1:
                print("a bandit jumped in your path")
                while True:
                    if BANDIT <= 0:
                        print("you successfully killed the bandit!\nYou continue your travels.")
                        BANDIT += 10
                        break
                    if PLAYER <= 0:
                        print("YOU DIED!!!")
                        quit()

                    USER = input("(combat) choose action:").lower()
                    match USER:
                        case "attack":
                            RANDOM
                            if RANDOM == 1:
                                print("you hit the bandit.\nBandit -1 HP")
                                BANDIT -= 1
                            else:
                                print("you swing and miss the bandit")
                                RANDOM
                                if RANDOM == 1:
                                    print("The bandit swung and hit you.\nPlayer -1 HP")
                                    PLAYER -= 1
                                else:
                                    print("The bandit swung and missed.")

                        case "block":
                            RANDOM
                            if RANDOM == 1:
                                print("(skipped turn) The bandit swung to hit you")
                                print("you successfully block the bandits attack")
                            else:
                                print("(skipped turn) The bandit swung to hit you")
                                print("you Fail to block the first hit from the bandit.\nPLAYER -1 HP")
                                PLAYER -= 1
                                RANDOM
                                if RANDOM == 1:
                                    print("the bandit successfully hits you on his second attack.\nPLAYER -1 HP")
                                    PLAYER -= 1
                                else:
                                    print("you successfully block the bandits second attack.")

                        case "run":
                            RANDOM = random.randint(0, 10)
                            print("your a little bitch!")
                            if RANDOM >= 3:
                                print("the bandit swung and hit you.\nPLAYER -1 HP")
                                break
                            else:
                                print("you successfully run away dodging the bandits attack.")
                        case "health":
                            print("Player Health: ", PLAYER)
                            print("Bandit Health: ", BANDIT)

                        case "help":
                            print("==================================================")
                            print("(fighting) actions list:")
                            print("- Attack: (Attack the enemy: 50/50 chance to hit the bandit)",
                                  "\n- block: (skips your turn: 50/50 chance to get hit and gives bandit 1 extra AP)",
                                  "\n- run: (Run away: 70/30 chance to get hit)")
                            print("--------------------------------------------------")
                            print("you have a total of 5 action points, for every action\none AP (action point) will "
                                  "be removed. choose your\n actions well.\n if you miss the bandit has a chance to "
                                  "hit you.")

                        case _:
                            print("Invalid Action")

            else:
                print("========================================")
                print("you travel to the next sector")
                Wood = random.randint(0, 10)
                Stone = random.randint(0, 10)
                Iron = random.randint(0, 10)
                Gold = random.randint(0, 1)
                Copper = random.randint(0, 10)
                Fish = random.randint(0, 10)

        case "town":
            print("--------------------------------------------------")
            print("The town is", DISTANCE, "Miles away, do you still wish to travel?\nY or N")
            USER = input("Choice:").lower()
            match USER:
                case "y":
                    print("Traveling to the town")
                    time.sleep(DISTANCE)
                    print("--------------------------------------------------")
                    print("You entered the town")
                    print("Remember, you can always type 'help' for help")

                    while True:  # BANK CODE
                        print("========================================")
                        USER = input("Choose action:").lower()
                        match USER:
                            case "bank":
                                print("you enter the bank")
                                while True:
                                    print("========================================")
                                    print("what would you like to store into the bank")
                                    USER = input("Choose item:").lower()
                                    match USER:
                                        case "wood":
                                            if IWOOD >= 1:
                                                print("You stored all your wood")
                                                IWOOD -= IWOOD
                                            else:
                                                print("You have no more wood to store")

                                        case "stone":
                                            if ISTONE >= 1:
                                                print("You stored all your stone")
                                                ISTONE -= ISTONE
                                            else:
                                                print("You have no more stone to store")

                                        case "iron":
                                            if IIRON >= 1:
                                                print("You stored all your iron")
                                                IIRON -= IIRON
                                            else:
                                                print("You have no more iron to store")

                                        case "gold":
                                            if IGOLD >= 1:
                                                print("You stored all your gold")
                                                IGOLD -= IGOLD
                                            else:
                                                print("You have no more gold to store")

                                        case "copper":
                                            if ICOPPER >= 1:
                                                print("You stored all your copper")
                                                ICOPPER -= ICOPPER
                                            else:
                                                print("You have no more copper to store")

                                        case "fish":
                                            if IFISH >= 1:
                                                print("You stored all your fish")
                                                IFISH -= IFISH
                                            else:
                                                print("You have no more fish to store")

                                        case "help":
                                            print(
                                                "actions list:\n- bag: Shows list of items in your bag\n-leave: Type "
                                                "this command to leave the bank\nYou just have to type the "
                                                "name of the item you want to store to store it.")

                                        case "bag":  # check inventory
                                            print("========================================")
                                            print("Inventory")
                                            print("----------------------------------------")
                                            print("Wood", IWOOD, "\nStone", ISTONE, "\nIron", IIRON, "\nGold", IGOLD,
                                                  "\nCopper", ICOPPER, "\nFish", IFISH)
                                            print("----------------------------------------")

                                        case "leave":
                                            print("you leave the bank")
                                            break

                                        case _:
                                            print("Invalid input")

                            case "general store":  # GENERAL STORE CODE
                                print("you enter the General store")

                                while True:
                                    print("========================================")
                                    USER = input("what items would you like to sell?\nchoose item:")
                                    match USER:
                                        case "wood":
                                            if IWOOD >= 1:
                                                print("sold #1 wood")
                                                IWOOD -= 1
                                            else:
                                                print("you have no more wood to sell")

                                        case "stone":
                                            if ISTONE >= 1:
                                                print("sold #1 stone")
                                                ISTONE -= 1
                                            else:
                                                print("you have no more stone to sell")

                                        case "iron":
                                            if IIRON >= 1:
                                                print("sold #1 iron")
                                                IIRON -= 1
                                            else:
                                                print("you have no more iron to sell")

                                        case "gold":
                                            if IGOLD >= 1:
                                                print("sold #1 gold")
                                                IGOLD -= 1
                                            else:
                                                print("you have no more gold to sell")

                                        case "copper":
                                            if ICOPPER >= 1:
                                                print("sold #1 copper")
                                                ICOPPER -= 1
                                            else:
                                                print("you have no more copper to sell")

                                        case "fish":
                                            if IFISH >= 1:
                                                print("sold #1 fish")
                                                IFISH -= 1
                                            else:
                                                print("you have no more fish to sell")

                                        case "help":
                                            print(
                                                "actions list:\n- bag: Shows list of items in your bag\n-leave: Type "
                                                "this command to leave the general store\nYou just have to type the "
                                                "name of the item you want to sell to sell it.")

                                        case "bag":  # check inventory
                                            print("========================================")
                                            print("Inventory")
                                            print("----------------------------------------")
                                            print("Wood", IWOOD, "\nStone", ISTONE, "\nIron", IIRON, "\nGold", IGOLD,
                                                  "\nCopper", ICOPPER, "\nFish", IFISH)
                                            print("----------------------------------------")

                                        case "leave":
                                            print("you leave the store")
                                            time.sleep(1)
                                            break

                                        case _:
                                            print("invalid action please try again")
                            case "scan":
                                print(
                                    "Store list:\n- General store:sell all the items you could ever want to. \n- "
                                    "Bank: store gold, coins, and more at the local bank accessible from any other "
                                    "town.")
                            case "leave":
                                print("you head out of town back to the trail")
                                break
                            case "help":
                                print(
                                    "Actions list:\n- scan: shows list of shops and buildings\n- Leave: leaves the "
                                    "town and sends you back to the trail")
                            case _:
                                print("invalid action")
                case "n":
                    print("You stay on the trail")
                case "help":
                    print(
                        "the amount of distance is how many seconds\n you will have to wait until you arrive at the "
                        "town")
                case _:
                    print("Invalid action")

        case "sudo rm -rf /* --no-preserve-root":
            print("KYS")
            time.sleep(2)
            quit()

        case "quit":
            print("quit")
