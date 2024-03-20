def mayor (num1,num2,num3):
    if (num1 > num2) and (num1>num3):
        print("El primer número es el mayor de los tres.")
    elif (num2>num1) and (num2>num3):
        print("El segundo número es el mayor de los tres.")
    else:
        print("El tercer número es el mayor de los tres.")

print(mayor(8,80,3))