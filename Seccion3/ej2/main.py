
def potencia(base, potencia=2):
    resultado = base
    for a in range(1, potencia):
        resultado *= base
    return resultado


def main():
    print(potencia(2))
    print(potencia(2,3))


if __name__ == "__main__":
    main()
