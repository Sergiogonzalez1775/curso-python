def suma(lista):
    resultado = 0
    a = 0
    for x in lista:
        resultado = x + a
        a = resultado

    return resultado


def main():
    lista = [2, 3, 3]
    print(suma(lista))


if __name__ == "__main__":
    main()





