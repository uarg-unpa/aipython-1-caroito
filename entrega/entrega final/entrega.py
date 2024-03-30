import random

def menu():
     print("Bienvenido al simulador de lanzamiento de dados.")
     print(f"1: Elegir tipos de dados") 
     print(f"2: Salir") 
     
def menu_dados():
    print(f"1: Para dados de 5 caras.") 
    print(f"2: Para dados de 7 caras.")
    print(f"3: Para dados de 10 caras.")
    print(f"4: Para dados de 15 caras.")
    print(f"5: Ingresar manualmente.")



def dado_5(cant_dados):
     resultados=[]
     for i in range(cant_dados):
          i = random.randint(1,5)
          print(f"El resultado del dado de 5 caras es: {i}")
          resultados.append(i) 
     print(f"Los resultados de los dados fueron: {resultados}") 
     total=sum(resultados)
     print(f"El total fue: {total}") 
    
def dado_7(cant_dados):
     resultados=[]
     for i in range(cant_dados):
          i = random.randint(1,7)
          print(f"El resultado del dado de 7 caras es: {i}") 
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


while True:
     op=0
     op1=0
     print(menu())
     op=int(input("Ingrese la opción: "))
     if op ==1:
         print(menu_dados())
         op1=int(input("Ingrese una opción: "))
     elif op ==2:
          print("Vuelva pronto!")
          break
     else:
          print("Ingrese una opción válida.")
     if op1>=1 and op1<=5:
          cant_dados=int(input("Cuántos dados desea tirar?: "))
     else:
          print("Por favor, ingrese una opción válida")
          print()
          continue
     if op1==1:
          dado_5(cant_dados)
     elif op1==2:
          dado_7(cant_dados)
     elif op1==3:
          dado_10(cant_dados)
     elif op1==4:
          dado_15(cant_dados)
     elif op1==5:
          dado_manual(cant_dados)
     else:
          print("Ingrese una opcion válida.")

     break