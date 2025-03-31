import string

texto=input("Introduzca un texto:")

mayusculas = 0

for letra in texto:
    if letra in string.ascii_uppercase:
        mayusculas += 1


print("se han encontrado {} mayusculas".format(mayusculas))