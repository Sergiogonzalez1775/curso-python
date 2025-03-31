import random


def adivinanza(numero):
    numero_ganador = random.randint(1, 100)

    if numero == numero_ganador:
        print("Has ganado!")
        return True
    else:
        print("Has perdido!")
        return False


def main():
    numero = int(input("Escoja un numero al alazar y pruebe suerte! "))
    while adivinanza(numero) is not True:
        numero = int(input("Escoja un numero al alazar y pruebe suerte! "))


if __name__ == "__main__":
    main()
