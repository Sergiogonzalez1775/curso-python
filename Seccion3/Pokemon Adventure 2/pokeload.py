from requests_html import HTMLSession
import pickle

pokemon_base = {
    "name": "",
    "current_health": 100,
    "base_health": 100,
    "level": 1,
    "type": None,
    "current_exp": 0
}

URL_BASE = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="

def get_pokemon(index):
    url = "{}{}".format(URL_BASE, index)
    session = HTMLSession()

    pokemon = pokemon_base.copy()
    pokemon_page = session.get(url)

    pokemon["name"] = pokemon_page.html.find(".mini", first = True).text

    pokemon["type"] = []

    for img in  pokemon_page.html.find(".bordeambos", first = True).find("img"):
        pokemon["type"].append(img.attrs["alt"])

    pokemon["attacks"] = []

    for attack_item in pokemon_page.html.find(".pkmain")[-1].find("tr .check3"):
        attack = {
            "name": attack_item.find("td", first = True).find("a", first = True).text,
            "type": attack_item.find("td")[1].find("img", first = True).attrs["alt"],
            "min_level": attack_item.find("th", first = True).text.replace("--","0"),
            "damage": int(attack_item.find("td")[3].text.replace("--","0"))
        }
        pokemon["attacks"].append(attack)

    return pokemon


def get_all_pokemons():
    try:
        print("Cargando archivo de pokemons")
        with open("pokefile.pkl", "rb") as pokefile:
            all_pokemons = pickle.load(pokefile)

    except FileNotFoundError:
        print("Archivo no encontrado, cargando de internet")
        all_pokemons = []
        for index in range(151):
            try:
                all_pokemons.append(get_pokemon(index+1))
                print("*", end = "")
            except AttributeError:
                print("\nPokemon {} no encontrado".format(index+1))


        with open("pokefile.pkl", "wb") as pokefile:
            pickle.dump(all_pokemons, pokefile)

        print("\nTodos los pokemos han sido descargados!!")

        print("Lista de pokemons cargada")

    return all_pokemons




