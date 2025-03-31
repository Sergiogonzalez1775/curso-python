def respuesta(nuevo_item, lista_de_la_compra):

    if nuevo_item in lista_de_la_compra:
        print("este producto ya existe en la lista")
    else:
        lista_de_la_compra.append(nuevo_item)
        print("Producto añadido")
        print(lista_de_la_compra)


def main():
    lista_de_la_compra = ["pan", "leche", "huevos"]
    nuevo_item = input("¿que producto desea añadir a la lista de la compra? ")
    respuesta(nuevo_item, lista_de_la_compra)


if __name__ == "__main__":
    main()


