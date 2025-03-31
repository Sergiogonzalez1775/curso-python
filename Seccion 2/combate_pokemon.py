from random import randint


titulo = "Combate Pokemon"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")



VIDA_INICIAL_PIKACHU=80
VIDA_INICIAL_SQUIRTLE=90
BARRA_DE_VIDA=10

vida_pikachu=VIDA_INICIAL_PIKACHU
vida_squirtle=VIDA_INICIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle >0:

    print("Turno de Pikachu")
    ataque_pikachu= randint(1,2)
    if ataque_pikachu == 1:
        print("Pikachu ha usado bola voltio")
        vida_squirtle -= 10

    else:
        print("Pikachu ha usado onda trueno")
        vida_squirtle -= 11

    input("...\n\n")

    if vida_pikachu < 0:
        vida_pikachu=0

    if vida_squirtle < 0:
        vida_squirtle=0

    barras_de_vida_pikachu = int(vida_pikachu * BARRA_DE_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:     [{}{}] ({}/{})".format("#" * barras_de_vida_pikachu, " " * (BARRA_DE_VIDA - barras_de_vida_pikachu),
                                            vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtle = int(vida_squirtle * BARRA_DE_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:    [{}{}] ({}/{})".format("#" * barras_de_vida_squirtle, " " * (BARRA_DE_VIDA - barras_de_vida_squirtle),
                                            vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("...\n\n")

    print("Turno de Squirtle")
    ataque_squirtle = None

    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle != "N":
        ataque_squirtle=input("Elige el ataque de Squirtle: [P]:Placaje, [A]:Pistola de Agua, [B]:Burbuja, [N]:Nada")

    if ataque_squirtle == "P":
        print("Squirtle ha usado placaje")
        vida_pikachu -= 10

    elif ataque_squirtle == "A":
       print("Squirtle ha usado pistola de agua")
       vida_pikachu -= 12

    elif ataque_squirtle == "B":
        print("Squirtle ha usado burbuja")
        vida_pikachu -=9
    elif ataque_squirtle == "B":
        print("Squirtle no ha usado ningun ataque")

    input("...\n\n")

    if vida_pikachu < 0:
        vida_pikachu=0

    if vida_squirtle < 0:
        vida_squirtle=0

    barras_de_vida_pikachu = int(vida_pikachu * BARRA_DE_VIDA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:     [{}{}] ({}/{})".format("#" * barras_de_vida_pikachu, " " * (BARRA_DE_VIDA - barras_de_vida_pikachu),
                                           vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtle = int(vida_squirtle * BARRA_DE_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:    [{}{}] ({}/{})".format("#" * barras_de_vida_squirtle, " " * (BARRA_DE_VIDA - barras_de_vida_squirtle),
                                            vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("...\n\n")

if vida_pikachu > vida_squirtle:
    print("Squirtle ha sido derrotado, el ganador es Pikachu")
else:
    print("Pikachu ha sido derrotado, el ganador es Squirtle")