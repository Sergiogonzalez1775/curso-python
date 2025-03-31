print("Bienvenido al programa")
n1 = int(input("Introduce el primer numero: "))
n2 = int(input("Introduce el segundo numero: "))
n3 = int(input("Introduce el tercer numero: "))
maximo = max(n1, n2, n3)
minimo = min(n1, n2, n3)
print("El numero maximo entre {}, {}, {} es {} y el numero minimo es {}".format(n1,
                                                                                n2,
                                                                                n3,
                                                                                maximo,
                                                                                minimo))