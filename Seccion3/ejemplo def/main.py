
def saludo_secreto(nombre):
        print("Hola {}".format(nombre[::-1]))

def largo_string(string):
    largo = 0

    for n in string:
        largo +=1

    return largo

saludo_secreto("Sergio")
largo_de_la_string = largo_string("12345")
print(largo_de_la_string)