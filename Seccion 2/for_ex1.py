texto=input("Introduzca un texto:")
espacios = 0
puntos = 0
comas = 0

for letra in texto:
    if letra == " ":
        espacios += 1

    elif letra == ".":
        puntos += 1

    if letra == ",":
        comas += 1

print("se han encontrado {} espacios".format(espacios))
print("se han encontrado {} puntos".format(puntos))
print("se han encontrado {} comas".format(comas))

