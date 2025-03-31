titulo = "Bienvenido al programa de conversion Moneda Internacional"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

dolar_euro = float(0.85)
euro_dolar = float(1.18)
libra_euro = float(1.10)
euro_libra = float(0.91)


opcion=input("¿Que tipo de conversion desea hacer?\n"
             "A - Dolar($) a Euro(€)\n"
             "B - Euro(€) a Dolar($)\n"
             "C - Libra(L) a Euro(€)\n"
             "D - Euro(€) a Libra(L)\n"
             "Seleccion:")


if opcion == "A":
    print("Ha seleccionado la ocion A, cambio de Dolar a Euro\n")
    cantidad = float(input("Introduce la cantidad que desea convertir:"))
    print("La cantidad en euros es: {}".format(cantidad * dolar_euro))
elif opcion == "B":
    print("Ha seleccionado la ocion A, cambio de Euro a Dolar\n")
    cantidad = float(input("Introduce la cantidad que desea convertir:"))
    print("La cantidad en dolares es: {}".format(cantidad * euro_dolar))
else:
    print("Opcion no valida")
    exit()


