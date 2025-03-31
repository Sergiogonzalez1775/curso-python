import os
import random
import readchar

NUM_OF_MAP_OBJECTS = 5
POS_X = 0
POS_Y = 1
NUM_MASTERS = [1, 2, 3, 4, 5]
INITIAL_LIFE_POKEMON_USER = 90
INITIAL_LIFE_POKEMON_CPU = None
LIFE_BAR = 10


def map_definition():
    style_map = """\
   ###         ###         
   ###         ###         
   ###         ###         
   ###   ###   ###   ###   
   ###   ###   ###   ###   
   ###   ###   ###   ###   
   ###   ###   ###   ###   
   ###   ###   ###   ###   
   ###   ###   ###   ###   
   ###   ###   ###   ###   
         ###         ###   
         ###         ###   
         ###         ###    \
"""

    style_map = [list(row) for row in style_map.split("\n")]
    return style_map


def generate_objects(map_objects, style_map, my_position, map_width, map_height):
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_object = [random.randint(0, map_width - 1), random.randint(0, map_height - 1)]

        if new_object not in map_objects and new_object != my_position and \
                style_map[new_object[POS_Y]][new_object[POS_X]] != "#":
            map_objects.append(new_object)


def draw_map(my_position, map_width, map_height, map_objects, style_map, combate):
    print(" " + "-" * map_width * 3 + " ")

    for cordinate_y in range(map_height):
        print("|", end="")
        for cordinate_x in range(map_width):

            char_to_draw = " "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == cordinate_x and map_object[POS_Y] == cordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    combate = True
                    map_objects.remove(object_in_cell)

            if style_map[cordinate_y][cordinate_x] == "#":
                char_to_draw = "#"

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print(" " + "-" * map_width * 3 + " ")
    return combate


def show_pokemon_life(life_pokemon_cpu, pokemon_name_cpu, initial_life_pokemon_cpu,
                      life_pokemon_user, pokemon_name_user):
    if life_pokemon_cpu < 0:
        life_pokemon_cpu = 0

    if life_pokemon_user < 0:
        life_pokemon_user = 0

    life_bar_pokemon_cpu = int(life_pokemon_cpu * LIFE_BAR / initial_life_pokemon_cpu)
    print("{}:     [{}{}] ({}/{})".format(pokemon_name_cpu, "#" * life_bar_pokemon_cpu,
                                          " " * (LIFE_BAR - life_bar_pokemon_cpu),
                                          life_pokemon_cpu, initial_life_pokemon_cpu))

    life_bar_pokemon_user = int(life_pokemon_user * LIFE_BAR / INITIAL_LIFE_POKEMON_USER)
    print("{}:     [{}{}] ({}/{})".format(pokemon_name_user, "#" * life_bar_pokemon_user,
                                          " " * (LIFE_BAR - life_bar_pokemon_user),
                                          life_pokemon_user, INITIAL_LIFE_POKEMON_USER))


def main():
    my_position = [2, 1]
    initial_life_pokemon_cpu = None
    pokemon_name_user = None
    pokemon_name_cpu = None
    pokemon_user = None
    attack_1_cpu = None
    attack_2_cpu = None
    attack_1_user = None
    attack_2_user = None
    attack_3_user = None
    map_objects = []
    end_game = False
    died = False
    win = False

    # definition of the map
    style_map = map_definition()
    map_width = len(style_map[0])
    map_height = len(style_map)

    # Start of the history
    os.system("clear")
    print("Vienvenido a la aventura Pokemon!\n")
    input("Enter para continuar...\n\n")
    os.system("clear")
    print(
        "En esta aventura tendrás que localizar a los entrenadores de la región y granarlos en un combate Pokemon. \n")
    input("Enter para continuar...\n\n")
    os.system("clear")
    print("Una vez que venzas a todos habras finalizado la aventura. \n")
    input("Enter para continuar...\n\n")
    os.system("clear")
    print("Antes de empezar tienes que escoger un Pokemon que te acompañe durante esta aventura. \n")
    input("Enter para continuar...\n\n")
    os.system("clear")

    # Selection of the pokemon of the user
    while pokemon_user != "1" and pokemon_user != "2" and pokemon_user != "3":
        pokemon_user = input(
            "Escoja qué pokemon quiere usar para esta aventura: [1]:Skirtle, [2]Charmander, [3]Bulbasaur ")

        if pokemon_user == "1":
            pokemon_name_user = "Skirtle"
            attack_1_user = "placaje"
            attack_2_user = "burbuja"
            attack_3_user = "pistola de agua"

        elif pokemon_user == "2":
            pokemon_name_user = "Charmander"
            attack_1_user = "placaje"
            attack_2_user = "ascuas"
            attack_3_user = "llamarada"

        elif pokemon_user == "3":
            pokemon_name_user = "Bulbasaur"
            attack_1_user = "placaje"
            attack_2_user = "hoja afilada"
            attack_3_user = "Latigo cepa"

    print("Has escogido a {} para esta aventura, sabia decisión!\n".format(pokemon_name_user))
    input("Enter para continuar...\n\n")
    os.system("clear")

    print("Ahora sal ahí fuera y rerrotalos a todos!\n".format(pokemon_name_user))
    input("Enter para continuar...\n\n")
    os.system("clear")

    # generate randome objects
    generate_objects(map_objects, style_map, my_position, map_width, map_height)

    # Main loop
    while not end_game:
        os.system("clear")
        combate = False

        # Draw map
        combate = draw_map(my_position, map_width, map_height, map_objects, style_map, combate)

        # Ask user where he wnats to move
        print("Moverse W:subir, S:bajar, A:izquierda, D:derecha")

        direction = readchar.readchar()
        new_position = None

        if direction == "w":
            new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % map_height]

        elif direction == "s":
            new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % map_height]

        elif direction == "a":
            new_position = [(my_position[POS_X] - 1) % map_width, my_position[POS_Y]]

        elif direction == "d":
            new_position = [(my_position[POS_X] + 1) % map_width, my_position[POS_Y]]

        elif direction == "q":
            end_game = True

        if new_position:
            if style_map[my_position[POS_Y]][new_position[POS_X]] != "#":
                my_position = new_position

        os.system("clear")

        # Pokemon battle
        if combate:
            print("Has encontrado un entrenador!\n")
            input("Enter para continuar...\n\n")
            os.system("clear")

            # rivals options definition
            pokemon = random.choice(NUM_MASTERS)
            NUM_MASTERS.remove(pokemon)

            if pokemon == 1:
                pokemon_name_cpu = "Pikachu"
                initial_life_pokemon_cpu = 80
                attack_1_cpu = "onda trueno"
                attack_2_cpu = "bola voltio"

            elif pokemon == 2:
                pokemon_name_cpu = "Nidoran"
                initial_life_pokemon_cpu = 40
                attack_1_cpu = "Placaje"
                attack_2_cpu = "Pua venenosa"

            elif pokemon == 3:
                pokemon_name_cpu = "Sperow"
                initial_life_pokemon_cpu = 20
                attack_1_cpu = "ataque rápido"
                attack_2_cpu = "ala filo"

            elif pokemon == 4:
                pokemon_name_cpu = "Abra"
                initial_life_pokemon_cpu = 60
                attack_1_cpu = "confusion"
                attack_2_cpu = "ataque psyquico"

            elif pokemon == 5:
                pokemon_name_cpu = "Ratata"
                initial_life_pokemon_cpu = 10
                attack_1_cpu = "mordisco"
                attack_2_cpu = "Placaje"

            print("El entrenador usará a {}!\n".format(pokemon_name_cpu))
            input("Enter para continuar...\n\n")
            os.system("clear")

            life_pokemon_cpu = initial_life_pokemon_cpu
            life_pokemon_user = INITIAL_LIFE_POKEMON_USER

            while life_pokemon_cpu > 0 and life_pokemon_user > 0:
                # Pokemon CPU turn
                print("Turno de {}\n".format(pokemon_name_cpu))
                ataque_pokemon_cpu = random.randint(1, 2)
                if ataque_pokemon_cpu == 1:
                    print("{} ha usado {}\n".format(pokemon_name_cpu, attack_1_cpu))
                    life_pokemon_user -= 10
                else:
                    print("{} ha usado {}\n".format(pokemon_name_cpu, attack_2_cpu))
                    life_pokemon_user -= 15

                input("Enter para continuar...\n\n")

                # Show life bar of the pokemons
                show_pokemon_life(life_pokemon_cpu, pokemon_name_cpu, initial_life_pokemon_cpu,
                                  life_pokemon_user, pokemon_name_user)

                if life_pokemon_user == 0:
                    break

                input("Enter para continuar...\n\n")
                os.system("clear")

                print("Turno de {}".format(pokemon_name_user))
                attack_pokemon_user = None

                while attack_pokemon_user != "1" and attack_pokemon_user != "2" and attack_pokemon_user != "3" and \
                        attack_pokemon_user != "0":
                    attack_pokemon_user = input(
                        "Elige el ataque: [1]:{}, [2]:{}, [3]:{}, [0]:Nada ".format(attack_1_user, attack_2_user,
                                                                                    attack_3_user))

                if attack_pokemon_user == "1":
                    print("{} ha usado {}\n".format(pokemon_name_user, attack_1_user))
                    life_pokemon_cpu -= 5

                elif attack_pokemon_user == "2":
                    print("{} ha usado {}\n".format(pokemon_name_user, attack_2_user))
                    life_pokemon_cpu -= 10

                elif attack_pokemon_user == "3":
                    print("{} ha usado {}\n".format(pokemon_name_user, attack_3_user))
                    life_pokemon_cpu -= 20

                elif attack_pokemon_user == "0":
                    print("{} no ha usado ningun ataque\n".format(pokemon_name_user))

                input("Enter para continuar...\n\n")

                # Show life bar of the pokemons
                show_pokemon_life(life_pokemon_cpu, pokemon_name_cpu, initial_life_pokemon_cpu,
                                  life_pokemon_user, pokemon_name_user)

                input("Enter para continuar...\n\n")
                os.system("clear")

            if life_pokemon_cpu > life_pokemon_user:
                os.system("clear")
                print("{} ha sido derrotado, el ganador es {}\n".format(pokemon_name_user, pokemon_name_cpu))
                input("Enter para continuar...\n\n")
                os.system("clear")
                end_game = True
                died = True

            else:
                os.system("clear")
                print("{} ha sido derrotado, el ganador es {}\n".format(pokemon_name_cpu, pokemon_name_user))
                input("Enter para continuar...\n\n")
                os.system("clear")

            if len(map_objects) == 0:
                end_game = True
                win = True

        os.system("clear")

    if died:
        print("Has sido derrotado!")

    if win:
        print("ENHORABUENA!!!")
        print("Has vencido a todos los entrenadores de la region!!!")


if __name__ == "__main__":
    main()
