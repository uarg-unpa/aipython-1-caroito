import random

def menu():
     mensaje="Bienvenido al simulador de lanzamiento de dados."
     return mensaje

def lanzar_dado(cant_dados):
    for i in range(cant_dados):
     caras=int(input("Ingrese cuántas caras va a tener el dado: "))
     i = random.randint(1,caras)
     print(f"El resultado del dado de {caras} caras es: {i}")




while True:
     print(menu())
     cant_dados=int(input("ingrese cuantos dados quiere tirar: "))
     lanzar_dado(cant_dados)
     break