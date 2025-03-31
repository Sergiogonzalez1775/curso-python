edad=int(input("Digame su edad: "))
tipo_de_carnet= input("Digame su tipo de carnet: ")

if (25 <= edad <= 35 and tipo_de_carnet == "E") or edad < 10 or (edad > 65 and tipo_de_carnet == "P") or (tipo_de_carnet == "F"):
    print("se te aplica el 25% de decuento.")
else:
    print("no se te aplica el descuento.")