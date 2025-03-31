def string_mas_larga(lista):
    resultado = 0

    palabra = ""

    for x in lista:
        largo = len(x)

        if largo > resultado:
            palabra = x

        resultado = largo

    return palabra


def main():
    lista = ["hola", "como", "estas"]
    print(string_mas_larga(lista))


if __name__ == "__main__":
    main()


