#listas
#creacion lista vacia
nombres=[]
#valores iniciales
nombres=['franco','fernanda','alejandro','fabiana']
#mostrar listas
print(nombres)
#iterar sobre la lista usando indices
for i in range(len(nombres)):
    print(nombres[i])
#accedemos a los elementos
#accedemos al primer elemento
primer_elemento=nombres[0]
print(f"el primer elemento es {primer_elemento}")


#creacion de listas usando el metodo
#nombres=list()
#crear una lista con valores iniciales
nombres=list(['gaston','eva','lautaro'])
print(nombres)

#metodos, append. permite agregar un elemento al final de la lista
nombres.append('sandra')
#print(nombres)

#insert
nombres.insert(0,'victoria')
#print(nombres)

#utilizar el operador in
for nombre in nombres:
    print(nombre)

#mutabilidad
print()
nombres[4]='lorenzo'
for nombre in nombres:
    print(nombre)
    print(id(nombres))
print()

