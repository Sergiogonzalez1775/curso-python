def potencia(numero, base=2):
    resultado = numero
    for a in range(1, base):
        resultado *= numero
    return resultado

def main():
    print(potencia(5))
    print(potencia(5, 5))

if __name__ == "__main__":
    main()


