su_edad = int(input("Ingrese su edad: "))
mi_edad = 19
diferencia = su_edad-mi_edad

if (su_edad>mi_edad):
    print("Usted es mayor que yo por",diferencia, "años.")
elif(su_edad<mi_edad):
    print("Usted es menor que yo por",(mi_edad-su_edad), "años.")
else:
    print ("Contemporáenos!")
