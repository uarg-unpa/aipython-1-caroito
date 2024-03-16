edad = int(input("Ingrese su edad:"))
ingreso = int(input("Ingrese sus ingresos:"))

if ((edad >= 18) and (ingreso >= 100000)):
    print("Usted debe pagar el impuesto")
else:
    print("Usted no debe pagar el impuesto")
