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

pais = input("introduce tu pais de origen:")
if pais == "argentina":
      input("ingrese su ciudad")
      if input() == "rio gallegos":
      else:
        print("bienvenido rio galleguense")




dia = input("ingrese un dia de la semana: ")
dia = dia.title()
match dia:
    case "Lunes":
          print("lunes")
    case "Martes":
          print("Martes")
    case "Miercoles":
          print("Miercoles")
    case "Jueves":
          print("Jueves")
    case "Viernes":
          print("Viernes")
    case _:
        print("no valido")