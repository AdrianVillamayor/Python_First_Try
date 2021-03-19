# Tipo de variables y condicionales

type_var = [2.1 ,1 ,"Aloha" ,'a', True];

print(type(type_var));

for x in type_var:
    print(type(x))

a = 1
if (a > 0 or a < 0) or (a != 0) and isinstance(a):
    print("Sip")
else :
    print("Nop")