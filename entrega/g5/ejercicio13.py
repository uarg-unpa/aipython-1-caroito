def encontrar_vocal(palabra):
    vocal=['a','e','i','o','u']
    b=0
    for a in palabra:
        if vocal in palabra:
            a+=1
    return a

print(encontrar_vocal("asdekliocuasd"))