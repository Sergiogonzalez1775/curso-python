import random
numero_ganador = random.randint(1, 10)
numero_elegido = int(input("Elige el numero: "))

if numero_elegido == numero_ganador:
    print("Has ganado!")
else:
    print("Has perdido!")

print("El numero ganador era: {}.".format(numero_ganador))