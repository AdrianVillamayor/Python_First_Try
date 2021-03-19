# Convertir de libras a € con valores dados por el usuario

libra = float(input("Valor en libras para convertir en euros "))
libra_euro = float(input("Valor del mercado de la libra "))

if libra != 0 or libra > 0:
    print("nice")

resultado = (libra * libra_euro)

print("{} libtras equivale a {} €".format(libra, resultado))
