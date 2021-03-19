# El programa pide por terminal un número del 1 al 10
# se recoge y se compara con un int random dentro del mismo 
# rango que el input

import random

winner_number = random.randint(1, 10)

chose_number = input("Un número del 1 al 10 \n")


if winner_number == int(chose_number):
    print("🏆")

else:
    print("Loser 💩 " + str(winner_number))
