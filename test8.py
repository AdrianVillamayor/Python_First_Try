
def generarOrdern():
    orden = input("Que necesitas comprar ?\n"
                  " - ")
    if(orden != "Nada" and orden != ''):
        x_orden = int(input("Cuanto unidades de {} necesitas comprar ? \n"
                            " - ".format(orden)))
        return [orden, x_orden]
    else:
        return "Nada"


def exportLista(lista):
    if len(lista) > 0:
        with open('compra.txt', 'w') as f:
            for x in lista:
                f.write("- {}, {} u. \n".format(x[0], x[1]))
    else:
        print("La lista esta vacia.")


def prepareList(lista_encode):
    lista_importada = []

    for x in lista_encode:
        x = x.replace(" ", "")
        x = x.replace("-", "")
        order = x.split(",")

        if order[0] != '':
            producto = order[0]
            cantidad = order[1].replace("u.", "")
            lista_importada.append([producto, cantidad])

    return lista_importada


def importLista(lista):
    lista = []
    if (input("Quieres exportar alguna lista que este en el mismo root (Y/N) ? \n"
              " - ")).upper() == "Y":
        try :

            with open('compra.txt', 'r') as f:
                line = f.read().split("\n")
                lista = prepareList(line)

            print("Lista importada con exito \n")
        except FileNotFoundError:
            print("El archivo compra.txt no existe.")

        return lista

def main():
    lista = []
    orden = ""

    lista = importLista(lista)
    print(lista)

    while orden == "" or orden != "Nada":
        orden = generarOrdern()
        if(orden != "Nada"):
            lista.append(orden)

    exportLista(lista)


if __name__ == "__main__":
    main()
