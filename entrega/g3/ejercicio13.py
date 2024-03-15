num =int(input("Ingrese un número:"))
suma=0
for i in range(0,num+1,2):
    print(i)
    suma= i+suma
print("La suma de los pares es: ",suma)