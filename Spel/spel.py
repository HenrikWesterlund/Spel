

import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()


def random1():
    x = random.randint(1, 10)
    return x


def random2(x):
    y = 10-x
    return y


class Player():
    def __init__(self, hp, stregth):
        self.hp = hp
        self.stregth = stregth

    def __str__(self):
        return f"HP:{self.hp} Strength:{self.stregth}"


hp1 = random1()
hp2 = random1()
hp3 = random1()

player1 = Player(hp1, random2(hp1))
player2 = Player(hp2, random2(hp2))
player3 = Player(hp3, random2(hp3))

meny_svar = input("""
1: Starta spelet
2: Regelboken
3: Avsluta
""")

clear()

if meny_svar == "1":
    print("Välj en karaktär som du vill starta med")
    print("1:" + str(player1))
    print("2:" + str(player2))
    print("3:" + str(player3))

while True:
    karaktär_svar = input("Val:")
    if karaktär_svar == "1":
        clear()
        print("Din karaktär har:\n" + str(player1))
        break

    elif karaktär_svar == "2":
        clear()
        print("Din karaktär har:\n" + str(player2))
        break

    elif karaktär_svar == "3":
        clear()
        print("Din karaktär har:\n" + str(player3))
        break

    else:
        print("Du måste välja 1, 2 eller 3")
