num=2
def multiplicacion(x):
    num=3
    return x*num
print(multiplicacion(4))

def mensaje():
    alternativo="mas sobre programacion"
    print("alumnos de aipython")
    return alternativo

dato = mensaje()
print(dato)

print()
def mutables(lista):
    lista[2]=35

mis_numeros=[1,2,3]
print(f"Antes de invocar a la funcion")
print(mis_numeros)
mutables(mis_numeros)
print(f"Después de invocar a la funcion")
print(mis_numeros)
print(id(mis_numeros))