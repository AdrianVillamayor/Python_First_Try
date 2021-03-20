
def potencia(num, *args, large_retunr=False):
    if args:
        potencia = []
        for x in args:
            potencia.append(pow(num, x))
    else:
        potencia = pow(num, 2)

    if large_retunr:
        return "La potencia del número {} es: {}".format(num, potencia)
    else:
        return potencia


def fibonacci(n, a=0, b=1):
    while n != 0:
        print("{} \n".format(a))
        return fibonacci(n-1, b, a+b)
    return a


def main():

    print(potencia(2))
    print(potencia(3, 4))
    print(potencia(8, 20, large_retunr=True))
    print(potencia(9, 200))

    fibonacci(5)


if __name__ == "__main__":
    main()
