print("Bienvenido al programa de conversion de temperatura de grados Fahrenheit a Celsius")
Gradosf = int(input("Introduce la temperatura en grados Fahrenheit que desea convertir:"))
GradosC = (Gradosf-32)*5/9
print("{} grados Fahrenheit son {} grados celsius".format(Gradosf,GradosC))