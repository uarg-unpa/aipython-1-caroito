su_edad = int(input("Ingrese su edad: "))
mi_edad = 2004

if (su_edad-mi_edad==1):
    print("Usted es menor que yo por un año.")
elif (su_edad==mi_edad):
    print("Contemporáneos!")
else:
    print("Usted es mayor que yo por",(mi_edad-su_edad), "años.")
