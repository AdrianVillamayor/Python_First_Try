repeat = input("Dime números separados por comas")

numbers = repeat.split(",")
print(numbers)

numbers = [int(numero) for numero in numbers]

print(numbers)
