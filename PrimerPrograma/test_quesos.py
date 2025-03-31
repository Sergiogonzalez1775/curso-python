titulo = "¿Cuánto te gusta el queso?"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")
puntos=0

print("PREGUNTA 1:\n")
opcion1=input("¿Que haces cuando ves una tabla de quesos?\n"
             "A - Salgo corriendo\n"
             "B - pruebo uno de los quesos o icluso varios\n"
             "C - No puedo evitar devorarla\n"
             "Seleccion:\n")

if opcion1 == "A":
    puntos += 0
elif opcion1 == "B":
    puntos += 5
elif opcion1 == "B":
    puntos += 10 
else:
    print("Opcion no valida")
    exit()

print("PREGUNTA 2:\n")
opcion2=input("¿Como te gusta la hamburguesa?\n"
             "A - Sin queso\n"
             "B - Con queso\n"
             "C - Con extra de queso\n"
             "Seleccion:\n")

if opcion2 == "A":
    puntos += 0
elif opcion2 == "B":
    puntos += 5
elif opcion2 == "C":
    puntos += 10
else:
    print("Opcion no valida")
    exit()

print("PREGUNTA 3:\n")
opcion3=input("¿Eres intolerante a la lactosa?\n"
             "A - Si\n"
             "B - A veces\n"
             "C - No\n"
             "Seleccion:\n")

if opcion3 == "A":
    puntos += 0
elif opcion3 == "B":
    puntos += 5
elif opcion3 == "B":
    puntos += 10
else:
    print("Opcion no valida")
    exit()

if puntos >= 25:
    print("Resultado: Te encanta el queso")
elif puntos >= 15:
    print("Resultado: Te gusta pero un poco")
else:
    print("Resultado: No te gusta nada el queso")
