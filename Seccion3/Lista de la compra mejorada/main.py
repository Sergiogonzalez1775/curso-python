
SALIDA = "SALIR"
LISTAR = "LISTA"
ARCHIVO_LISTA = "lista_compra.txt"
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
    with open(ARCHIVO_LISTA, "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))


def guardar_item_en_lista(lista_compra, nuevo_item):
    if nuevo_item.lower() in [a.lower() for a in lista_compra]:
        print("El producto ya existe")
    else:
        lista_compra.append(nuevo_item)


def cargar_archivo():
    lista_compra = []
    if input("Quieres cargar la ultima lista de la compra? [SI/NO]"):
        try:
            with open(ARCHIVO_LISTA, "r") as a:
                lista_compra = a.read().split("\n")
        except FileNotFoundError:
            print("Archivo de la compra no encontrado")
    return lista_compra


def mostrar_lista(lista_compra):
    print("\n".join(lista_compra))


def main():
    lista_compra = cargar_archivo()
    mostrar_lista(lista_compra)
    nuevo_item = input_usuario()

    while nuevo_item != SALIDA:
        if nuevo_item == LISTAR:
            print("\n".join(BASE_DE_DATOS))
            nuevo_item = input_usuario()

        else:
            guardar_item_en_lista(lista_compra, nuevo_item)
            mostrar_lista(lista_compra)
            nuevo_item = input_usuario()



    insert_on_file(lista_compra)


if __name__ == "__main__":
    main()
