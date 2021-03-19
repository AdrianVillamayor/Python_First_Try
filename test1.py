# Buscar el número más grande y pequeño de un grupo
# dado por el usuario

num = [0, 0, 0]

for i in [0, 1, 2]:
    num[i] = int(input("Dime un número [" + str(i) + "]"))

print("Número Mayor => " + str(max(num)))
print("Número Menor => " + str(min(num)))
