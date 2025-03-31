lista_de_la_compra = []
input_de_usuario = None

titulo = "Lita de la compra"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

while True:
    input_de_usuario = input("¿Qué desea comprar? (Utilice [Q] para salir): ")
    if input_de_usuario == "Q":
        break
    elif input_de_usuario in lista_de_la_compra:
        print("El producto {} ya está en la lista".format(input_de_usuario))
    else:
        if input("¿Está seguro de que quiere añadir {} a la lista? [S/N]".format(input_de_usuario)) == "S":
            lista_de_la_compra.append(input_de_usuario)

print("La lista de la compra es:")
print(lista_de_la_compra)



