import os
import random
import readchar

MAP_WIDTH = ''
MAP_HEIGHT = ''

while (MAP_HEIGHT == '' and MAP_WIDTH == ''):
    MAP_WIDTH = input("Dime el ancho del mapa: ")
    MAP_HEIGHT = input("Dime el alto del mapa: ")

MAP_WIDTH = int(MAP_WIDTH)
MAP_HEIGHT = int(MAP_HEIGHT)

#       x  y
user = [0, 0]
lvl = 1

symbols = {"user": '▪', 'fruit': '⌾', 'empty': ' ',
           'bar': '│', 'top': '⎽', 'bottom': '⎺'}

action = ""
symbol = " "
points = 0
tail = []


def checkFruits(x, y, fruits):

    if [x, y] not in fruits:
        return True
    else:
        x = random.randint(1, (MAP_WIDTH - 1))
        y = random.randint(1, (MAP_HEIGHT - 1))
        if checkFruits(x, y, fruits):
            return x, y


def setFruits(lvl):

    fruits = []

    for i in range((2 * lvl)):
        x = random.randint(1, (MAP_WIDTH - 1))
        y = random.randint(1, (MAP_HEIGHT - 1))
        if checkFruits(x, y, fruits):
            fruits.append([x, y])

    return fruits


fruits = setFruits(lvl)


def draw_map(MAP_HEIGHT, MAP_WIDTH, user, tail):
    global points

    print(symbols['top'] * (MAP_WIDTH + 2))

    for y in range(MAP_HEIGHT):
        print(symbols['bar'], end="")

        for x in range(MAP_WIDTH):

            if x == user[0] and y == user[1]:
                symbol = symbols['user']
            else:
                symbol = symbols['empty']

            for fruit in fruits:
                if x == fruit[0] and y == fruit[1]:
                    symbol = symbols['fruit']
                    if(user[0] == fruit[0] and user[1] == fruit[1]):
                        points += 1
                        fruits.remove([fruit[0], fruit[1]])
                        symbol = symbols['user']

            for tail_piece in tail:
                if x == tail_piece[0] and y == tail_piece[1]:
                    symbol = symbols['user']

            print("{}".format(symbol), end="")

        print(symbols['bar'])

    print(symbols['bottom'] * (MAP_WIDTH + 2))

    print("Nivel: {} \n".format(lvl))
    print("Puntos: {} \n".format(points))
    print("ESC para salir")

    return points


def resetGame():
    global user
    global lvl
    global fruits

    user = [0, 0]
    lvl += 1
    fruits = setFruits(lvl)
    print("Nivel {} superado, vamos a por el siguiente". format(lvl))


while True:
    os.system("clear")

    draw_map(MAP_HEIGHT, MAP_WIDTH, user, tail)

    if len(fruits) == 0:
        resetGame()

    else:
        direction = readchar.readkey()

        if direction == "w" or direction == "\x1b[A":
            tail.insert(0, user.copy())
            tail = tail[:points]

            actual_y = user[1]
            user[1] -= 1
            user[1] %= MAP_HEIGHT

        elif direction == "s" or direction == '\x1b[B':
            tail.insert(0, user.copy())
            tail = tail[:points]

            actual_y = user[1]
            user[1] += 1
            user[1] %= MAP_HEIGHT

        elif direction == "d" or direction == '\x1b[C':
            tail.insert(0, user.copy())
            tail = tail[:points]

            actual_x = user[0]
            user[0] += 1
            user[0] %= MAP_WIDTH

        elif direction == "a" or direction == '\x1b[D':
            tail.insert(0, user.copy())
            tail = tail[:points]

            actual_x = user[0]
            user[0] -= 1
            user[0] %= MAP_WIDTH

        elif direction == '\x1b\x1b':
            break

print("End Game")
