titulo = "¿Que telefono movil te deberías comprar?"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

SO=input("¿Que sistema operativo prefieres?\n"
         "A - Android\n"
         "I - IOS\n"
         "Seleccion:")

if SO == "A":
    dinero = input("¿tienes dinero? [Y/N]\n")
    if dinero == "N":
        print("Tu telefono apropiado es un Android chino de 100€")
    elif dinero == "Y":
        camara= input("¿Te importa la camara del movil?[Y/N]\n")
        if camara == "Y":
            print("Tu telefono apropiado es un Google pixel super camara")
        elif dinero == "Y":
            print("Tu telefono apropiado es un Android calidad-precio")
        else:
            print("Opcion no valida")
            exit()
    else:
        print("Opcion no valida")
        exit()
elif SO == "I":
    dinero = input("¿tienes dinero? [Y/N]\n")
    if dinero == "Y":
        print("Tu telefono apropiado es un iphone ultra PRO MAX")
    elif dinero == "N":
        print("Tu telefono apropiado es un iphone de segunda mano")
    else:
        print("Opcion no valida")
        exit()
else:
    print("Opcion no valida")
    exit()