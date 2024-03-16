def factorial(num):
    resultado = 1
    for i in range(num,resultado,-1):
        resultado = i*resultado
    print(f"El factorial de {num} es {resultado}.")

print(factorial(4))