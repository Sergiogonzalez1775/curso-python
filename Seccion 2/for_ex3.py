numero=int(input("Introduzca un numero para multiplicar:"))
resultado = 0

for n in range(1, 11):
    if n % 2 == 0:
        print("{}x2{}={}".format(n, numero,n + numero))



