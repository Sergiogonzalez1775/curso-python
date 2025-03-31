
def main(cantidad, valor):
    resultado = cantidad * valor
    print("La cantidad {} son {} €".format(cantidad, resultado))


if __name__ == "__main__":
    cantidad = float(input("¿que cantidad quieres cambiar en euros?: "))
    valor = float(input("¿cuanto vale su dinero en euros?: "))
    main(cantidad, valor)
