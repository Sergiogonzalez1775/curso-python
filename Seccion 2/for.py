vocales=['a','e','i','o','u']
frase="Hola Mundo!"
vocles_encontradas=0

for letra in frase:
    if letra in vocales:
        print("He encontrado la letra {}".format(letra))
        vocles_encontradas += 1

print("se han encontrado {} vocales".format(vocles_encontradas))