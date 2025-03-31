def mayus(string):
    cadena_convertida = ""

    for a in string:
        if a == "a":
            a = "A"
            cadena_convertida += a
        elif a == "b":
            a = "B"
            cadena_convertida += a
        elif a == "c":
            a = "C"
            cadena_convertida += a
        elif a == "d":
            a = "D"
            cadena_convertida += a
        elif a == "e":
            a = "E"
            cadena_convertida += a
        elif a == "f":
            a = "F"
            cadena_convertida += a
        elif a == "g":
            a = "G"
            cadena_convertida += a
        elif a == "h":
            a = "H"
            cadena_convertida += a
        elif a == "i":
            a = "I"
            cadena_convertida += a
        elif a == "j":
            a = "J"
            cadena_convertida += a
        elif a == "k":
            a = "K"
            cadena_convertida += a
        elif a == "l":
            a = "L"
            cadena_convertida += a
        elif a == "m":
            a = "M"
            cadena_convertida += a
        elif a == "n":
            a = "N"
            cadena_convertida += a
        elif a == "ñ":
            a = "Ñ"
            cadena_convertida += a
        elif a == "o":
            a = "O"
            cadena_convertida += a
        elif a == "p":
            a = "P"
            cadena_convertida += a
        elif a == "q":
            a = "Q"
            cadena_convertida += a
        elif a == "r":
            a = "R"
            cadena_convertida += a
        elif a == "s":
            a = "S"
            cadena_convertida += a
        elif a == "t":
            a = "T"
            cadena_convertida += a
        elif a == "u":
            a = "U"
            cadena_convertida += a
        elif a == "v":
            a = "V"
            cadena_convertida += a
        elif a == "w":
            a = "W"
            cadena_convertida += a
        elif a == "x":
            a = "X"
            cadena_convertida += a
        elif a == "y":
            a = "Y"
            cadena_convertida += a
        elif a == "z":
            a = "Z"
            cadena_convertida += a
        else:
            cadena_convertida += a
    return cadena_convertida


def main():
    string = input("escriba la frase que desea convertir a mayuscualas")
    print(mayus(string))


if __name__ == "__main__":
    main()



