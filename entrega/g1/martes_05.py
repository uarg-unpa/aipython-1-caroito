#edad = 19
#print (F"su edad es: {edad}")

texto ="EstO eS UN tExTO MeZclAdO"
#title
print(texto.title())
print(texto)
texto = texto.title()
print (texto)

#upper lower
print(texto.upper())
print(texto.lower())

#replace
print(texto.replace(" ","."))

print(len(texto))

edad= int(input("ingrese su edad: "))
if (edad>=18):
    print("usted debe votar")
else:
    print("usted es menor")
print("linea independiente")

calificacion = int(input("ingrese su calificacion: "))
if (calificacion >= 90):   
    print("excelente")
elif (calificacion>=80):
        print("bien")
elif (calificacion>=70):
        print("bien")
else:
        print("insuficiente")