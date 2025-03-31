import random

NUM_MASTERS = [1, 2, 3, 4, 5]
INITIAL_LIFE_POKEMON_USER = 90
INITIAL_LIFE_POKEMON_CPU = None
LIFE_BAR = 10

pokemon_name_user = ""
pokemon_name_cpu = ""
attack_1_cpu = ""
attack_2_cpu = ""
attack_1_user = ""
attack_2_user = ""
attack_3_user = ""


pokemon_user = input("Escoja que pokemon quiere usar para esta aventura: [1]:Skirtle, [2]Charmander, [3]Bulbasaur")

while pokemon_user != "1" and pokemon_user != "2" and pokemon_user != "3":
    if pokemon_user == "1":
        pokemon_name_user = "Skirtle"
        attack_1_user = "placaje"
        attack_2_user = "burbuja"
        attack_3_user = "pistola de agua"

    if pokemon_user == "2":
        pokemon_name_user = "Charmander"
        attack_1_user = "placaje"
        attack_2_user = "ascuas"
        attack_3_user = "llamarada"

    if pokemon_user == "3":
        pokemon_name_user = "Bulbasaur"
        attack_1_user = "placaje"
        attack_2_user = "hoja afilada"
        attack_3_user = "Latigo cepa"

print("Sabia decisión! Has escogido a {} para esta aventura".format(pokemon_name_user))

title = "Combate Pokemon"
print("\n" + title + "\n" + "-" * len(title) + "\n")

while len(NUM_MASTERS) > 0:
    #rivals options definition
    pokemon = random.choice(NUM_MASTERS)

    if pokemon == 1:
        pokemon_name_cpu = "Pikachu"
        INITIAL_LIFE_POKEMON_CPU = 80
        attack_1_cpu = "onda trueno"
        attack_2_cpu = "bola voltio"

    elif pokemon == 2:
        pokemon_name_cpu = "Nidoran"
        INITIAL_LIFE_POKEMON_CPU = 40
        attack_1_cpu = "Placaje"
        attack_2_cpu = "Pua venenosa"

    elif pokemon == 3:
        pokemon_name_cpu = "Sperow"
        INITIAL_LIFE_POKEMON_CPU = 20
        attack_1_cpu = "ataque rápido"
        attack_2_cpu = "ala filo"

    elif pokemon == 4:
        pokemon_name_cpu = "Abra"
        INITIAL_LIFE_POKEMON_CPU = 60
        attack_1_cpu = "confusion"
        attack_2_cpu = "ataque psyquico"

    elif pokemon == 5:
        pokemon_name_cpu = "Ratata"
        INITIAL_LIFE_POKEMON_CPU = 10
        attack_1_cpu = "mordisco"
        attack_2_cpu = "Placaje"

    life_pokemon_cpu = INITIAL_LIFE_POKEMON_CPU
    life_pokemon_user = INITIAL_LIFE_POKEMON_USER

    while life_pokemon_cpu > 0 and life_pokemon_user > 0:

        #Pokemon CPU turn
        print("Turno de {}".format(pokemon_name_cpu))
        ataque_pikachu = random.randint(1, 2)
        if life_pokemon_user == 1:
            print("{} ha usado {}".format(pokemon_name_cpu, attack_1_cpu))
            life_pokemon_user -= 10

        else:
            print("{} ha usado {}".format(pokemon_name_cpu, attack_2_cpu))
            life_pokemon_user -= 15

        input("Enter para continuar...\n\n")

        if life_pokemon_cpu < 0:
            vida_pokemon_cpu = 0

        if life_pokemon_user < 0:
            vida_pokemon_usuario = 0

        life_bar_pokemon_cpu = int(life_pokemon_cpu * LIFE_BAR / INITIAL_LIFE_POKEMON_CPU)
        print("{}:     [{}{}] ({}/{})".format(pokemon_name_cpu, "#" * life_bar_pokemon_cpu,
                                              " " * (LIFE_BAR - life_bar_pokemon_cpu),
                                              life_pokemon_cpu, INITIAL_LIFE_POKEMON_CPU))

        life_bar_pokemon_user = int(life_pokemon_user * LIFE_BAR / INITIAL_LIFE_POKEMON_USER)
        print("{}:    [{}{}] ({}/{})".format(pokemon_name_user, "#" * life_bar_pokemon_user,
                                             " " * (LIFE_BAR - life_bar_pokemon_user),
                                             life_pokemon_user, INITIAL_LIFE_POKEMON_USER))

        input("Enter para continuar...\n\n")

        print("Turno de {}".format(pokemon_name_user))
        attack_pokemon_user = None

        while attack_pokemon_user != "P" and attack_pokemon_user != "A" and attack_pokemon_user != "B" and \
                attack_pokemon_user != "N":
            attack_pokemon_user = input("Elige el ataque: [1]:{}, [2]:{}, [3]:{}, [N]:Nada ".format(attack_1_user, attack_2_user, attack_3_user))

        if attack_pokemon_user == "1":
            print("{} ha usado {}".format(pokemon_name_user, attack_1_user))
            life_pokemon_cpu -= 5

        elif attack_pokemon_user == "2":
            print("{} ha usado {}".format(pokemon_name_user, attack_2_user))
            life_pokemon_cpu -= 10

        elif attack_pokemon_user == "3":
            print("{} ha usado {}".format(pokemon_name_user, attack_3_user))
            life_pokemon_cpu -= 20

        elif attack_pokemon_user == "N":
            print("{} no ha usado ningun ataque".format(pokemon_name_user))

        input("Enter para continuar...\n\n")

        if life_pokemon_cpu < 0:
            vida_pikachu = 0

        if life_pokemon_user < 0:
            vida_pokemon_usuario = 0

        life_bar_pokemon_cpu = int(life_pokemon_cpu * LIFE_BAR / INITIAL_LIFE_POKEMON_CPU)
        print("{}:     [{}{}] ({}/{})".format(pokemon_name_cpu, "#" * life_bar_pokemon_cpu,
                                              " " * (LIFE_BAR - life_bar_pokemon_cpu),
                                              life_pokemon_cpu, INITIAL_LIFE_POKEMON_CPU))

        life_bar_pokemon_user = int(life_pokemon_user * LIFE_BAR / INITIAL_LIFE_POKEMON_USER)
        print("{}:    [{}{}] ({}/{})".format(pokemon_name_user, "#" * life_bar_pokemon_user,
                                             " " * (LIFE_BAR - life_bar_pokemon_user),
                                             life_pokemon_user, INITIAL_LIFE_POKEMON_USER))

        input("Enter para continuar...\n\n")

    if life_pokemon_cpu > life_pokemon_user:
        print("{} ha sido derrotado, el ganador es {}".format(pokemon_name_user, pokemon_name_cpu))
    else:
        print("{} ha sido derrotado, el ganador es {}".format(pokemon_name_cpu, pokemon_name_user))

print("Has derrotado a todos los entrenadores de la region")
