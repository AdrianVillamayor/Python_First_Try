
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
                f.write("- {}, {} unidad \n".format(x[0], x[1]))
    else:
        print("La lista esta vacia.")


def main():
    lista = []
    orden = ""

    while orden == "" or orden != "Nada":
        orden = generarOrdern()
        if(orden != "Nada"):
            lista.append(orden)

    exportLista(lista)


if __name__ == "__main__":
    main()
