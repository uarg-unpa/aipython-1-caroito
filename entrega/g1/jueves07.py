#inmutables
cadena="AIPYTHON"
print(cadena[5])

#frase = input("Ingrese una frase: ")
#caracter = input("Ingrese un caracter: ")

#busca la primera aparicion del caracter
#posicion= frase.find(caracter)
# !=diferente o igual a
#if posicion != 1 :
 #   print(f"el caracter{caracter} se encuentra en la posicion {posicion+1}")
  #  subcadena= frase[posicion:]
   # print(f"subcadena a partir de la posicion {posicion+1}: {subcadena}")
#else:
#    print(f"el caracter {caracter} no se encuentra en la frase")

contador = 0

while (contador <= 10):
    print(contador)
    contador += 1
print ("fin de la iteracion")

cadena = "aipyhton"
for letra in cadena:
    print(letra)

for num in range (10):
    print(num)

for indice in range(len(cadena)):
    print(cadena[indice])

for num in range (0,11,2):
    print(num)

for _ in range (5):
    print("caro")