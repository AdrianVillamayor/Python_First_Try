
def checkPar(num):
    if(num % 2 == 0):
        return True
    else:
        return False


def charCount(*args):
    count = 0
    palabra = ""
    if args:
        for x in args:
            len_string = len(x)

            if count < len_string:
                count = len_string
                palabra = x
    else:
        palabra = "No has introducido ninguna palabra."
    return palabra


def sumatorio(*args):
    sumatorio = 0

    if args:
        for x in args:
            sumatorio += x
    else:
        sumatorio = "No has introducido ninguna número."
    return sumatorio

def checkRespuesta():
    respuesta = input("Estas seguro (Y/N) ?").upper()

    if(respuesta == 'Y'):
        return True
    else:
        return False


def main():
    print("-"*20)

    palabra = charCount("Hola", "Adrian", "Sandra", 'Yela',
                        'Paradas', 'Villamayor', 'Sanchez', '!')
    if palabra != "No has introducido ninguna palabra.":
        print("La palabra más larga es: {} con una logitud de {} \n".format(
            palabra, len(palabra)))
    else:
        print(palabra)

    print("-"*20)

    tula = (1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 12, 43, 55)
    sumatorio_ = sumatorio(1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 12, 43, 55)

    if sumatorio_ != "No has introducido ninguna número.":
        print("La suma total de los números {} es {} \n".format(
            tula, sumatorio_))
    else:
        print(palabra)

    print("-"*20)

    num_check = 14
    if checkPar(num_check):
        print("El número {} es par \n".format(
            num_check))
    else:
          print("El número {} no es par \n".format(
            num_check))
   
    print("-"*20)

    respuesta = checkRespuesta()
    print(type(respuesta), respuesta)

if __name__ == "__main__":
    main()
