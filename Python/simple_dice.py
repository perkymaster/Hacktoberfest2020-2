import random

print("Here is a simple dice simulator")

x="x"

while x=="x":

    number=random.randint(1,6)

    if number == 1:
        print("----------")
        print("|        |")
        print("|    X   |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| X    X |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    X   |")
        print("|    X   |")
        print("|    X   |")
        print("----------")
    if number == 4:
        print("----------")
        print("| X    X |")
        print("|        |")
        print("| X    X |")
        print("----------")
    if number == 5:
        print("----------")
        print("| X    X |")
        print("|    X   |")
        print("| X    X |")
        print("----------")
    if number == 6:
        print("----------")
        print("| X    X |")
        print("| X    X |")
        print("| X    X |")
        print("----------")
    x = input("Press x to roll again or Press e to quit the simulation")
    if x=="e":
        quit
