
contraseña = input("Ingrese su contraseña: ")
contraseña_guardada = (input("Ingrese de nuevo su contraseña: "))
contraseña = contraseña.lower()
contraseña_guardada = contraseña_guardada.lower()

if (contraseña == contraseña_guardada): 
    print("las contraseñas son iguales.")
else:
    print("Las contraseñas son diferentes.")