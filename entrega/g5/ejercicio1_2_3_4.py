#ejercicio1
lista_vacia = []
print (lista_vacia)

print()

#ejercicio2
colores = list(['Negro','Blanco','Rojo','Azul','Anaranjado','Amarillo', 'Verde'])
print(colores)

print()

#ejercicio3
print("La longitud de la lista 'colores' es:",len(colores))
print()

#ejercicio4
frutas = list(['Naranja','Mandarina','Banana','Pera','Kiwi'])
#a
print("Longitud:",len(frutas))
#b
print("Antes de eliminar un elemento: ",frutas)
del frutas[0]
print("Después de eliminar el primer elemento: ",frutas)
#b
frutas.append('Pelon')
print(frutas)