#15.Escribir un programa que pida un número entero e informe si dicho número es
#primo o no primo
num =int(input("Ingrese un número entero: "))
i =2
while num % i != 0:
    i += 1
if i == num:
    print("es primo")
else:
    print("no es primo")