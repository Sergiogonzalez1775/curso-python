import random
import os
from pokeload import get_all_pokemons

COMBAT = {
    "player_pokemon": None,
    "enemy_pokemon": None,
    "combat_number": 0
}

WEAKNESSES = {
    "normal": ["lucha"],
    "fuego": ["agua", "tierra", "roca"],
    "agua": ["planta", "eléctrico"],
    "planta": ["fuego", "hielo", "veneno", "volador", "bicho"],
    "eléctrico": ["tierra"],
    "hielo": ["fuego", "lucha", "roca", "acero"],
    "lucha": ["volador", "psíquico", "hada"],
    "veneno": ["tierra", "psíquico"],
    "tierra": ["agua", "planta", "hielo"],
    "volador": ["eléctrico", "hielo", "roca"],
    "psíquico": ["bicho", "fantasma", "siniestro"],
    "bicho": ["volador", "roca", "fuego"],
    "roca": ["agua", "planta", "lucha", "tierra", "acero"],
    "fantasma": ["fantasma", "siniestro"],
    "dragón": ["hielo", "dragón", "hada"],
    "siniestro": ["lucha", "bicho", "hada"],
    "acero": ["fuego", "lucha", "tierra"],
    "hada": ["veneno", "acero"]
}

STRENGTHS = {
    "fuego": ["planta", "hielo", "bicho", "acero"],
    "agua": ["fuego", "tierra", "roca"],
    "planta": ["agua", "tierra", "roca"],
    "eléctrico": ["agua", "volador"],
    "hielo": ["tierra", "volador", "dragón"],
    "lucha": ["normal", "hielo", "roca", "siniestro", "acero"],
    "veneno": ["planta", "hada"],
    "tierra": ["fuego", "eléctrico", "veneno", "roca", "acero"],
    "volador": ["lucha", "bicho"],
    "psíquico": ["lucha", "veneno"],
    "bicho": ["planta", "psíquico", "siniestro"],
    "roca": ["fuego", "hielo", "volador", "bicho"],
    "fantasma": ["psíquico"],
    "siniestro": ["psíquico", "fantasma"],
    "acero": ["hielo", "roca", "hada"],
    "hada": ["lucha", "dragón", "siniestro"]
}


LIFE_BAR = 10


def get_player_profile(pokemon_list):
    return  {
        "Player_name": input("¿Cuál es tu nombre?"),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "Pokeballs": 4,
        "health_poison": 4
    }


def check_type_handicap(attack_type, defender_type):
    points = 0

    for strength in STRENGTHS.get(attack_type, "Tipo no encontrado\n"):
        if strength == defender_type:
            points += 1

    for weakness in WEAKNESSES.get(attack_type, "Tipo no encontrado\n"):
        if weakness == defender_type:
            points -= 1

    if points > 0:
        handicap = 1,25

    elif points == 0:
        handicap = 1

    else:
        handicap = 0,75

    return handicap


def clear_and_continue():
    input("Enter para continuar...\n\n")
    os.system("clear")


def choose_pokemon(player_profile):
    chosen = None

    while not chosen:
        for index in range(len(player_profile["pokemon_inventory"])):
            if player_profile["pokemon_inventory"][index]["current_health"] > 0:
                print("{} - {}\n".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index])))

        try:
            return int(input("¿Cual eliges?\n"))

        except (ValueError, IndexError):
            print("Opcion no valida\n")
            clear_and_continue()


def show_pokemon_life(player_pokemon, enemy_pokemon):

    life_bar_pokemon_cpu = int(enemy_pokemon["current_health"] * LIFE_BAR / enemy_pokemon["base_health"])
    print("{}:     [{}{}] ({}/{})".format(enemy_pokemon["name"], "#" * life_bar_pokemon_cpu,
                                          " " * (LIFE_BAR - life_bar_pokemon_cpu),
                                          enemy_pokemon["current_health"], enemy_pokemon["base_health"]))

    life_bar_pokemon_user = int(player_pokemon["current_health"] * LIFE_BAR / player_pokemon["base_health"])
    print("{}:     [{}{}] ({}/{})".format(player_pokemon["name"], "#" * life_bar_pokemon_user,
                                          " " * (LIFE_BAR - life_bar_pokemon_user),
                                          player_pokemon["current_health"], player_pokemon["base_health"]))


def get_pokemon_info(pokemon):
    return "{} | lvl {} | hp {}/{}".format(pokemon["name"], pokemon["level"], pokemon["current_health"], pokemon["base_health"])


def show_inventory(player_profile, combats, player_pokemon, enemy_pokemon):
    option = None
    while option != 4:
        while option not in ["1", "2", "3", "4", "5", "6"]:
            try:
                option = input("Opciones:\n"
                                   "[1]Inventario\n"
                                   "[2]Combates realizados\n"
                                   "[3]Estado del combate\n"
                                   "[4]Estado de mis pokemons\n"
                                   "[5]Continuar\n"
                                    "[6]SALIR DEL JUEGO\n")

                if option not in ["1", "2", "3", "4", "5", "6"]:
                    print("Opción no valida")
                    option = None
                    continue

            except ValueError:
                print("Opción no valida")
                option = None
                continue

        if option == "1":
            print("Pokeballs: {}\n".format(player_profile["Pokeballs"]))
            print("Pociones de vida: {}\n".format(player_profile["health_poison"]))
            clear_and_continue()
            option = None
            continue

        elif option == "2":
            if len(combats) > 0:
                for combat in combats:
                    print("Combates hasta el momento\n")
                    print("{} - {} vs. {}".format(combat["combat_number"],combat["player_pokemon"],combat["enemy_pokemon"]))

            else:
                print("No has participado en ningun combate aún\n")

            clear_and_continue()
            option = None
            continue

        elif option == "3":
            show_pokemon_life(player_pokemon, enemy_pokemon)
            clear_and_continue()
            option = None
            continue

        elif option == "4":
            for pokemon in player_profile["pokemon_inventory"]:
                print(get_pokemon_info(pokemon))
            clear_and_continue()
            option = None
            continue

        elif option == "5":
            clear_and_continue()
            return

        elif option == "6":
            raise SystemExit("Saliendo del juego...")


def player_attack(player_pokemon, enemy_pokemon):
    print("Turno para {}\n".format(player_pokemon["name"]))
    clear_and_continue()

    print("Escoja un atauqe:\n")
    for attack in player_pokemon["attacks"]:
        index = player_pokemon["attacks"].index(attack)

        try:
            if player_pokemon["level"] >= int(attack["min_level"]):
                print("[{}]{} - {} - {}\n".format(index, attack["name"], attack["type"], attack["damage"]))

        except ValueError:
            attack["min_level"] = 1

            if player_pokemon["level"] >= int(attack["min_level"]):
                print("[{}]{} - {} - {}\n".format(index, attack["name"], attack["type"], attack["damage"]))

    selection = -1

    while selection < 0 or selection >= len(player_pokemon["attacks"]):
        try:
            selection = int(input("Ataque seleccionado:"))

        except ValueError:
            print("Ataque no encontrado")
            continue

    clear_and_continue()

    attack_name = player_pokemon["attacks"][selection]["name"]
    attack_type = player_pokemon["attacks"][selection]["type"]
    damage = player_pokemon["attacks"][selection]["damage"]

    handicap = check_type_handicap(attack_type,enemy_pokemon["type"])

    damage_total = handicap * damage
    enemy_pokemon["current_health"] -= damage_total

    print("{} ha usado {}[{}]\n".format(player_pokemon["name"], attack_name,damage_total))

    if handicap > 1:
        print("El ataque ha sido muy eficiente\n")

    elif handicap == 1:
        print("El ataque ha funcionado\n")

    else:
        print("El ataque no ha sido muy eficiente\n")

    clear_and_continue()

    if enemy_pokemon["current_health"] < 0 or enemy_pokemon["current_health"] == 0:
        enemy_pokemon["current_health"] = 0
        print("{} ha sido derrotado".format(enemy_pokemon["name"]))
        return enemy_pokemon

    return enemy_pokemon


def enemy_attack(enemy_pokemon, player_pokemon):
    print("Turno para {}\n".format(enemy_pokemon["name"]))
    clear_and_continue()

    try:
        selection = random.randint(0, len(enemy_pokemon["attacks"])-1)

    except IndexError:
        selection = 0

    attack_name = enemy_pokemon["attacks"][selection]["name"]
    attack_type = enemy_pokemon["attacks"][selection]["type"]
    damage = enemy_pokemon["attacks"][selection]["damage"]

    handicap = check_type_handicap(attack_type,player_pokemon["type"])

    try:
        damage_total = handicap * damage

    except IndexError:
        damage_total = handicap * enemy_pokemon["attacks"][0]["damage"]

    player_pokemon["current_health"] -= damage_total

    print("{} ha usado {}[{}]\n".format(enemy_pokemon["name"], attack_name, damage_total))

    if handicap > 1:
        print("El ataque ha sido muy eficiente\n")

    elif handicap == 1:
        print("El ataque ha funcionado\n")

    else:
        print("El ataque no ha sido muy eficiente\n")

    clear_and_continue()

    if player_pokemon["current_health"] < 0 or player_pokemon["current_health"] == 0:
        player_pokemon["current_health"] = 0
        print("{} ha sido derrotado".format(player_pokemon["name"]))
        return player_pokemon

    return player_pokemon


def add_attack_history(attack_history, index):
    attack_history.append(index)
    attack_history =  list(set(attack_history))
    return attack_history


def assign_experience(player_profile, attack_history):

    for index in attack_history:
        points = random.randint(1, 5)
        player_profile["pokemon_inventory"][index]["current_exp"] += points

        if player_profile["pokemon_inventory"][index]["current_exp"] > 20:
            player_profile["pokemon_inventory"][index]["current_exp"] -= 20
            player_profile["pokemon_inventory"][index]["level"] += 1
            player_profile["pokemon_inventory"][index]["current_health"] = player_profile["pokemon_inventory"][index]["base_health"]
            print("Tu pokemon ha subido al nivel {}\n".format(player_profile["pokemon_inventory"][index]["level"]))
            clear_and_continue()

    return player_profile


def cure_pokemon(player_profile):

    if player_profile["health_poison"] > 0:
        print("Escoja el poquemon al que le quiere aplicar la pocion")
        selection = choose_pokemon(player_profile)
        clear_and_continue()

        pokemon = player_profile["pokemon_inventory"][selection]

        pokemon["current_health"] += 50

        if pokemon["current_health"] > pokemon["base_health"]:
            pokemon["current_health"] = pokemon["base_health"]

        player_profile["pokemon_inventory"][selection]["current_health"] = pokemon["current_health"]

        print("La vida de {} ha aumentado a {}\n".format(pokemon["name"],  pokemon["current_health"]))
        clear_and_continue()

        player_profile["health_poison"] -= 1

        return player_profile, pokemon["current_health"]

    else:
        print("No tienes pociones en el inventario\n")
        clear_and_continue()


def capture_with_pokeball(player_profile, enemy_pokemon):
    captured = False
    if player_profile["Pokeballs"] > 0:
        if enemy_pokemon["current_health"] > enemy_pokemon["current_health"]/2:
            probability = random.randint(0, 10)

            if probability > 4:
                captured = True
                player_profile["pokemon_inventory"].append(enemy_pokemon)
                print("Has capturado a {}\n".format(enemy_pokemon["name"]))
                clear_and_continue()
                return player_profile, captured

            else:
                print("El pokemon ha escapado\n")
                clear_and_continue()
                return player_profile, captured

        else:
            print("El pokemon ha escapado\n")
            clear_and_continue()
            return player_profile, captured

    else:
        print("No tienes pokebals en el inventario\n")
        clear_and_continue()
        return player_profile, captured


def fight(player_profile, enemy_pokemon):
    print(" -- NUEVO COMBATE -- ")

    attack_history = []

    print("Elige con que pokemon lucharas\n")
    clear_and_continue()
    selected_pokemon_index = choose_pokemon(player_profile)
    player_pokemon = player_profile["pokemon_inventory"][selected_pokemon_index]
    print ("Contrincantes: {} vs. {}".format(get_pokemon_info(player_pokemon),
                                             get_pokemon_info(enemy_pokemon)))

    clear_and_continue()

    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0:
        action = None

        while action not in ["A","P","V","C"]:
            action = input("Que deseas hacer: [A]tacar, [P]okeball, Poción de [V]ida, [C]ambiar\n").upper()

            if action not in ["A","P","V","C"]:
                print("Opción no valida\n")
                clear_and_continue()

        clear_and_continue()

        if action == "A":
            enemy_pokemon = player_attack(player_pokemon, enemy_pokemon)
            attack_history = add_attack_history(attack_history, selected_pokemon_index)
            show_pokemon_life(player_pokemon, enemy_pokemon)
            clear_and_continue()

        elif action == "V":
            player_profile, player_pokemon["current_health"] = cure_pokemon(player_profile)

        elif action == "P":
            player_profile, captured = capture_with_pokeball(player_profile, enemy_pokemon)

            if captured:
                player_profile = assign_experience(player_profile, attack_history)
                player_profile = item_lottery(player_profile)
                return player_profile, player_pokemon

            else:
                print("el pokemon ha huido")
                return player_profile, player_pokemon

        elif action == "C":
            print("Elige con que pokemon lucharas\n")

            clear_and_continue()

            selected_pokemon_index = choose_pokemon(player_profile)
            player_pokemon = player_profile["pokemon_inventory"][selected_pokemon_index]

        if enemy_pokemon["current_health"] == 0:
            print("Has ganado!")

            player_profile = assign_experience(player_profile, attack_history)
            player_profile = item_lottery(player_profile)

            return player_profile, player_pokemon

        player_pokemon = enemy_attack(enemy_pokemon, player_pokemon)
        player_profile["pokemon_inventory"][selected_pokemon_index] = player_pokemon
        show_pokemon_life(player_pokemon, enemy_pokemon)
        clear_and_continue()

        if player_pokemon["current_health"] == 0 and any_player_pokemon_lives(player_profile):
            print("Elige con que pokemon lucharas\n")
            clear_and_continue()
            selection = choose_pokemon(player_profile)
            player_pokemon = player_profile["pokemon_inventory"][selection]


    print(" -- FINAL DEL COMBATE -- ")
    return player_profile, player_pokemon


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def item_lottery(player_profile):
    print("Veamos que te depara la suerte!!!")
    lottery = random.randint(0, 2)

    if lottery == 0:
        print("Otra vez será")
        clear_and_continue()
        return player_profile

    elif lottery == 1:
        player_profile["Pokeballs"] += 1
        print("Enhorabuena, te ha tocado una pokeball")
        clear_and_continue()
        return player_profile

    elif lottery == 2:
        player_profile["health_poison"] += 1
        print("Enhorabuena, te ha tocado una poción de vida")
        clear_and_continue()
        return player_profile


def main():
    clear_and_continue()
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)

    combats = []

    player_pokemon = player_profile["pokemon_inventory"][0]

    while any_player_pokemon_lives(player_profile):
        player_profile["combats"] += 1

        enemy_pokemon = random.choice(pokemon_list)
        show_inventory(player_profile, combats, player_pokemon, enemy_pokemon)
        combat = COMBAT.copy()

        player_profile, player_pokemon = fight(player_profile, enemy_pokemon)

        combat["player_pokemon"] = player_pokemon["name"]
        combat["enemy_pokemon"] = enemy_pokemon["name"]
        combat["combat_number"] += player_profile["combats"]

        combats.append(combat)

    print("Has perdido en el combate numero {}" .format(player_profile["combats"]))


if __name__ == "__main__":
    main()