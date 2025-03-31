
def main(numero):
    resultado = numero * numero
    print("la potencia de {} es {}".format(numero, resultado))


if __name__ == "__main__":
    numero = float(input("¿que numero quieres calcular su potencia?: "))
    main(numero)