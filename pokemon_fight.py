import random
import time
import os
from pprint import pprint


class Pokemon:
    def __init__(self, name, hp, attack, defense, speed, attaks) -> None:
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.attacks = attaks

    def turn(self):
        print("----------------\n")
        print("Seleccióna un ataque de {}\n".format(self.name))
        print("----------------\n")

        text_attacks = ""
        i = 0

        for x in self.attacks:
            text_attacks = text_attacks + \
                "{}: {} ({} ATTK) \n".format(i, x[0], x[1])
            i += 1

        attack = -1
        len_attacks = len(self.attacks)

        while attack < 0 or attack >= len_attacks:
            try:
                attack = int(input(text_attacks + "\n - "))
            except ValueError:
                attack = -1

        return int(attack)

    def summary(self):
        print(pprint(vars(self)))


pikachu = Pokemon("Pikachu",
                  35,
                  55,
                  40,
                  90,
                  [
                      ["Moflete estático", 20, "enemy_speed_down_1.2"],
                      ['Atizar', 80, None],
                      ['Trueno', 110, None],
                      ['Agilidad', 0, "self_speed_up_1.2"]
                  ])

squirtle = Pokemon("Squirtle",
                   44,
                   48,
                   65,
                   43,
                   [
                       ["Placaje", 40, None],
                       ['Pistola agua', 40, None],
                       ['Defensa férrea', 0, "self_defense_up_1.2"],
                       ['Hidrobomba', 110, None]
                   ])

turno = 1
first = ""
attack = ""


def checkSpeed(pokemon_1, pokemon_2):
    if(pokemon_1.speed > pokemon_2.speed):
        return pokemon_1.name
    elif(pokemon_1.speed < pokemon_2.speed):
        return pokemon_2.name
    elif (pokemon_1.speed == pokemon_2.speed):

        random_number = random.randint(0, 10)

        if(random_number % 2 == 0):
            return pokemon_1.name

        elif (random_number % 2 == 1):
            return pokemon_2.name


def attack_turn(attack, pokemon_1, pokemon_2):
    name = pokemon_1.attacks[attack][0]
    dmg = pokemon_1.attacks[attack][1]
    effect = pokemon_1.attacks[attack][2]

    if(dmg > 0):
        damage = attack_defense(dmg, pokemon_1.attack, pokemon_2.defense)
        if pokemon_2.hp - damage < 0:
            pokemon_2.hp = 0
        else:
            pokemon_2.hp = pokemon_2.hp - damage

    if(effect != None):
        attack_effect(effect, pokemon_1, pokemon_2)
    else:
        print("----------------\n")

    if(dmg > 0):
        print("{} ha usado el ataque {}, {} ha recibido {} de daño\n".format(
            pokemon_1.name, name, pokemon_2.name, damage))
    else:
        print("{} ha usado el ataque {}, {} no ha recibido daño\n".format(
            pokemon_1.name, name, pokemon_2.name))

    print("----------------\n")

    time.sleep(2)


def attack_defense(dmg, attack, defense):
    v = random.randint(85, 100)

    front = 0.01 * 1 * 1 * v
    top = (0.2 * 1 + 1) * attack * dmg
    bottom = 25 * defense

    damage = round(front * ((top / bottom) + 2))

    if damage == 0:
        damage = 1

    return damage


def attack_effect(effect, pokemon_1, pokemon_2):

    effect = effect.split("_")
    pokemon_ = None

    who = effect[0]
    attribute = effect[1]
    direction = effect[2]
    value = float(effect[3])

    if who == 'self':
        pokemon_ = pokemon_1
    else:
        pokemon_ = pokemon_2

    if attribute == "speed":
        speed(direction, pokemon_, value)
    elif attribute == "defense":
        defense(direction, pokemon_, value)
    else:
        return False

    print("----------------\n")
    print("* La {} de {} ha cambiado \n ".format(
        attribute.upper(), pokemon_.name))

    time.sleep(2)


def speed(direction, pokemon, value):
    if direction == "up":
        pokemon.speed = pokemon.speed * value
    else:
        pokemon.speed = pokemon.speed / value

    pokemon.speed = round(pokemon.speed)


def defense(direction, pokemon, value):
    if direction == "up":
        pokemon.defense = pokemon.defense * value
    else:
        pokemon.defense = pokemon.defense / value

    pokemon.defense = round(pokemon.defense)


def resumen(pokemon_1, pokemon_2, turno):
    print("----------------\n")
    print("FIN TURNO {}\n".format(turno))

    print("*{}\n".format(pokemon_1.name))
    pokemon_1.summary()

    print("*{}\n".format(pokemon_2.name))
    pokemon_2.summary()

    print("----------------\n")

    time.sleep(3)
    os.system("clear")


def endGame(pokemon_1, pokemon_2):
    text = ""
    if pokemon_1.hp <= 0:
        text = "{} ha ganado el combate".format(pokemon_2.name)
    elif pokemon_2.hp <= 0:
        text = "{} ha ganado el combate".format(pokemon_1.name)
    else:
        text = "Empate entre {} y {}".format(pokemon_1.name, pokemon_2.name)

    return text


while pikachu.hp > 0 and squirtle.hp > 0:
    print("----------------\n")
    print("INICIO DEL TURNO {}\n".format(turno))
    print("----------------\n")

    first = checkSpeed(pikachu, squirtle)

    if first == pikachu.name:
        attack = pikachu.turn()
        attack_turn(attack, pikachu, squirtle)

        if(squirtle.hp == 0):
            break

        attack = squirtle.turn()
        attack_turn(attack, squirtle, pikachu)

        if(pikachu.hp == 0):
            break

    elif first == squirtle.name:
        attack = squirtle.turn()
        attack_turn(attack, squirtle, pikachu)

        if(pikachu.hp == 0):
            break

        attack = pikachu.turn()
        attack_turn(attack, pikachu, squirtle)

        if(squirtle.hp == 0):
            break

    resumen(pikachu, squirtle, turno)

    turno += 1


print(endGame(pikachu, squirtle))
