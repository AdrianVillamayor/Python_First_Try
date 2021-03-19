# Print type, condicionales en un test de Queso

title = "Aloha, preparado para saber cuanto te gusta el queso ?"

print("\n {} \n {} \n".format(title, ("-" * len(title))))

puntnacion = 0
opt = [0, 0, 0]


opt[0] = input("""Pregunta 1: Que haces cunado ves una tabla de quesos? \n
            A - Salgo corriendo \n
            B - Pruebo uno o varios de los quesos \n
            C - No puedo evitar devorarla
            """)


opt[1] = input("Pregunta 2: Como te gusta la hamburguesa? \n"
               "A - Sin queso \n"
               "B - Con queso \n"
               "C - Mucho queso \n"
               )

opt[2] = input("Pregunta 3: Eres intolerante a la lactosa? \n"
               "A - Si \n"
               "B - Un poco \n"
               "C - No \n"
               )

for x in opt:
    if x.upper() == "A":
        puntnacion = puntnacion + 0
    elif x.upper() == "B":
        puntnacion = puntnacion + 5
    elif x.upper() == "C":
        puntnacion = puntnacion + 10

if puntnacion > 25:
    print("Puntuación: {} | Eres un queso lover".format(puntnacion))
elif puntnacion <= 25 and puntnacion > 15:
    print("Puntuación: {} | Te gusta el queso".format(puntnacion))
elif puntnacion <= 15:
    print("Puntuación: {} | No te gusta el queso".format(puntnacion))
