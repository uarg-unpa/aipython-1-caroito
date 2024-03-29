import random

def menu():
     mensaje="Bienvenido al simulador de lanzamiento de dados."
     return mensaje

def lanzar_dado(cant_dados):
    resultados=[]
    for i in range(cant_dados):
     caras=int(input("Ingrese cuántas caras va a tener el dado: "))
     i = random.randint(1,caras)
     print(f"El resultado del dado de {caras} caras es: {i}")
     resultados.append(i) 
    print(f"Los resultados de los dados fueron: {resultados}") 


while True:
     print(menu())
     cant_dados=int(input("Ingrese cuantos dados desea tirar: "))
     lanzar_dado(cant_dados)
     break