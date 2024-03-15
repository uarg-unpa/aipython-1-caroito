#14.Escribir un programa que recibe como entrada desde el usuario dos números
#enteros e imprimir todos los números pares entre ellos.
num = int(input("Ingrese un número entero: "))
num1 = int(input("Ingrese un segundo número entero: "))
for i in range(num,num1):
    if i%2 ==0:
        print (i)    
