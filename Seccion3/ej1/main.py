

def cambiador(cantidad, valor):
    resultado = cantidad * valor
    print("La cantidad {} son {} €".format(cantidad, resultado))


def main():
    cantidad = float(input("¿que cantidad quieres cambiar en euros?: "))
    valor = float(input("¿cuanto vale su dinero en euros?: "))
    cambiador(cantidad, valor)


if __name__ == "__main__":
    main()
