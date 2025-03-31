def respuesta():
    respuesta = None
    while respuesta != "Y" and respuesta != "N":
        respuesta = input("¿Está usted seguro? [Y/N] ")

    if respuesta == "Y":
        return True
    else:
        return False


def main():
    print(respuesta())


if __name__ == "__main__":
    main()


