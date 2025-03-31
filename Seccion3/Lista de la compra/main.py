
SALIDA = "SALIR"
LISTAR = "LISTA"
BASE_DE_DATOS = ["pan", "leche", "huevos", "harina", "azucar"]


def input_usuario():
    producto = input("¿que producto desea añadir a la lista de la compra? [pulse {} para salir o {}]".format(SALIDA,
                                                                                                             LISTAR))
    while producto.lower() not in BASE_DE_DATOS and producto != SALIDA and producto != LISTAR:
        print("producto no disponible para añadir en la lista")
        producto = input("¿que producto desea añadir a la lista de la compra? [pulse {} para salir o {}]".format(SALIDA,
                                                                                                             LISTAR))
    return producto


def insert_on_file(lista_compra):
    file_name = input("¿Como quieres que se llame el nompre del archivo?")
    with open(file_name + ".txt", "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))

    # mi_archivo = open(file_name + ".txt", "w")
    # mi_archivo.write("\n".join(lista_compra))
    # mi_archivo.close()


def main():
    lista_compra = []
    nuevo_item = input_usuario()
    while nuevo_item != SALIDA:
        if nuevo_item == LISTAR:
            print("\n".join(BASE_DE_DATOS))
            nuevo_item = input_usuario()
        else:
            lista_compra.append(nuevo_item)
            print("\n".join(lista_compra))
            nuevo_item = input_usuario()

    insert_on_file(lista_compra)


if __name__ == "__main__":
    main()
