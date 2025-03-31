import random
import os
from pokeload import get_all_pokemons

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
#---------------------------------------------------------------------


def get_player_profile(pokemon_list):
    return  {
#        "Player_name": input("¿Cuál es tu nombre?"),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "Pokeballs": 0,
        "health_poison": 1
    }

def clear_and_continue():
    input("Enter para continuar...\n\n")
    os.system("clear")



def item_lottery(player_profile):
    print("Veamos que te depara la suerte!!!")
    lottery = random.randint(0, 2)

    if lottery == 0:
        print("Otra vez será")
        clear_and_continue()

    elif lottery == 1:
        player_profile["Pokeballs"] += 1
        print("Enhorabuena, te ha tocado una pokeball")
        clear_and_continue()


    elif lottery == 2:
        player_profile["health_poison"] += 1
        print("Enhorabuena, te ha tocado una poción de vida")
        clear_and_continue()

    return player_profile


def get_pokemon_info(pokemon):
    return "{} | lvl {} | hp {}/{}".format(pokemon["name"], pokemon["level"], pokemon["current_health"], pokemon["base_health"])

def choose_pokemon(player_profile):
    chosen = None
    while not chosen:
        for index in range(len(player_profile["pokemon_inventory"])):
            if player_profile["pokemon_inventory"][index]["current_health"] > 0:
                print("{} - {}\n".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index])))
        try:
            selection = int(input("¿Cual eliges?\n"))
            return selection, player_profile["pokemon_inventory"][selection]
        except (ValueError, IndexError):
            print("Opcion no valida\n")
            clear_and_continue()

def cure_pokemon(player_profile):

    if player_profile["health_poison"] > 0:
        print("Escoja el pokmon al que le quiere aplicar la pocion")
        selection, pokemon = choose_pokemon(player_profile)

        pokemon = player_profile["pokemon_inventory"][selection]

        pokemon["current_health"] += 50



        player_profile["pokemon_inventory"][selection]["current_health"] = pokemon["current_health"]

        player_profile["health_poison"] -= 1

        print("La vida de {} ha aumentado a {}\n".format(pokemon["name"],  pokemon["current_health"]))
        clear_and_continue()

        return player_profile

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

def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)

    attack_history = [0]

    for i in range(20):
        player_profile = assign_experience(player_profile, attack_history)
        print(player_profile["pokemon_inventory"][0]["level"])
        print(player_profile["pokemon_inventory"][0]["current_exp"])












if __name__ == "__main__":
    main()