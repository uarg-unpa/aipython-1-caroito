import random

def menu():
     print("Bienvenido al simulador de lanzamiento de dados.")
     print(f"1: Elegir tipos de dados") 
     print(f"2: Jugar")
     print(f"3: Salir")     
     
def menu_dados():
    print(f"1: Para dados de 5 caras.") 
    print(f"2: Para dados de 6 caras.")
    print(f"3: Para dados de 10 caras.")
    print(f"4: Para dados de 15 caras.")
    print(f"5: Ingresar manualmente.")


def menu_juego():
    print(f"1: Reglas.") 
    print(f"2: Jugar.")


def reglas_juego():
     print("Tendrás que adivinar si el número generado del 1 al 100, será par o impar.")
     print("- - - - - - - - - - - - - - - -")
     print()


def dado_5(cant_dados):
     resultados=[]
     for i in range(cant_dados):
          i = random.randint(1,5)
          print(f"El resultado del dado de 5 caras es: {i}")
          resultados.append(i) 
     print(f"Los resultados de los dados fueron: {resultados}") 
     total=sum(resultados)
     print(f"El total fue: {total}") 
    
def dado_6(cant_dados):
     resultados=[]
     for i in range(cant_dados):
          i = random.randint(1,6)
          print(f"El resultado del dado de 6 caras es: {i}") 
          resultados.append(i) 
     print(f"Los resultados de los dados fueron: {resultados}") 
     total=sum(resultados)
     print(f"El total fue: {total}") 

def dado_10(cant_dados):
     resultados=[]
     for i in range(cant_dados):
          i = random.randint(1,10)
          print(f"El resultado del dado de 10 caras es: {i}")      
          resultados.append(i) 
     print(f"Los resultados de los dados fueron: {resultados}") 
     total=sum(resultados)
     print(f"El total fue: {total}") 

def dado_15(cant_dados):
     resultados=[]
     for i in range(cant_dados):
          i = random.randint(1,15)
          print(f"El resultado del dado de 15 caras es: {i}") 
          resultados.append(i) 
     print(f"Los resultados de los dados fueron: {resultados}") 
     total=sum(resultados)
     print(f"El total fue: {total}") 

def dado_manual(cant_dados):
    resultados=[]
    for i in range(cant_dados):
     caras=int(input("Ingrese cuántas caras va a tener el dado: "))
     i = random.randint(1,caras)
     print(f"El resultado del dado de {caras} caras es: {i}")
     resultados.append(i) 
    print(f"Los resultados de los dados fueron: {resultados}") 
    total=sum(resultados)
    print(f"El total fue: {total}") 

def juego(eleccion):
     numero = random.randint(1,100)

     if eleccion ==1:
          if numero%2 ==0:
               print("Ganaste! el número es par :)")
          else:
               print("Perdiste, el número es impar :(")
     elif eleccion == 2:
          if numero%2 != 0:
               print("Ganaste! el número es impar :)")
          else:
               print("Perdiste, el número es par :(")     

     print(f"El número era {numero}.")


cant_ope=0
while True:
     op=0
     op1=0
     op_juego=0
     print(menu())
     op=int(input("Ingrese una opción: "))
     if op ==1:
         print(menu_dados())
         op1=int(input("Ingrese una opción: "))
     elif op ==2:
          menu_juego()
          op_juego=int(input("Ingrese una opción:"))
     elif op==3:
          print("Vuelva pronto!")
          print("- - - - - - - - - - - - - - - -")
          break
     else:
          print("Ingrese una opción válida.")
     
     if op_juego==1:
          reglas_juego()
          continue
     
     elif op_juego ==2:
          eleccion= int(input("Ingrese 1 para par o 2 para impar: "))
          juego(eleccion)
          cant_ope +=1
          

     if op1>=1 and op1<=5:
          cant_dados=int(input("Cuántos dados desea tirar?: "))

     if op1==1:
          dado_5(cant_dados)
          cant_ope +=1
     elif op1==2:
          dado_6(cant_dados)
          cant_ope +=1
     elif op1==3:
          dado_10(cant_dados)
          cant_ope +=1
     elif op1==4:
          dado_15(cant_dados)
          cant_ope +=1
     elif op1==5:
          dado_manual(cant_dados)
          cant_ope +=1
     #else:
      #    print("Ingrese una opcion válida.")
     print(f"La cantidad de operaciones realizadas fue {cant_ope}")
     print("- - - - - - - - - - - - - - - -")
     continue