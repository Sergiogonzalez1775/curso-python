"""
numero_de_usuario = []

numero_introducido = int(input("Introduzca un numero a la lista: "))
numero_de_usuario.append(numero_introducido)
"""
while input("¿Desea introducir mas numeros? [S/N] ") == "S":
    numero_introducido = int(input("Introduzca un numero a la lista: "))
    numero_de_usuario.append(numero_introducido)

numeros_introducidos = input("Introduzca los numeros de la lista separados por coma: ")
numero_de_usuario = [int(numero) for numero in numeros_introducidos.split(",")]

numero_menor = numero_de_usuario[0]
numero_mayor = numero_de_usuario[0]

for numero in numero_de_usuario[1:]:
    if numero_menor > numero:
        numero_menor = numero

    if numero_mayor < numero:
        numero_mayor = numero

print("el numero grande es {}".format(numero_mayor))
print("el numero pequeño es {}".format(numero_menor))
