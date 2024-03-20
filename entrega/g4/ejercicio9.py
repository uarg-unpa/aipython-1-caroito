def invertir(palabra):
    alreves=palabra[::-1]
    if palabra == alreves:
        print(f"La palabra {palabra} es palíndromo!")
    else:
        print("Su palabra no es un palíndromo.")

print(invertir("pollo"))