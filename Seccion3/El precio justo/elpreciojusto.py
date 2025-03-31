import random
from io import BytesIO
from PIL import Image
from speak_and_listen import speak, hear_me
from requests_html import HTMLSession


#Funcion que escuha y obtiene el precio que dicen los jugadores
def hear_price_and_get_num():
    while True:
        try:
            price = hear_me()
            price.replace(" €", "").replace(",", ".").replace(" con ", ".")
            final_price = float(price)
            return final_price
        except ValueError:
            speak("No te he entendido, repite")

#Funcion que obtiene las categorias
def get_pccom_categories(session):
    main_url = "https://www.pccomponentes.com/"
    main_site = session.get(main_url)
    return main_site.html.find(".typography_typography_body2Regular__80yx6e4")

def get_selected_category(category1, category2, category3, category4, category5):
    while True:
        try:
            selection = hear_me()

            if selection ==  category1:
                return category1
            elif selection ==  category2:
                return category2
            elif selection ==  category3:
                return category3
            elif selection ==  category4:
                return category4
            elif selection ==  category5:
                return category5
            else:
                speak("La selección no coincide con ninguna categoría de la lista, seleccione una de nuevo")

        except ValueError:
            speak("No te he entendido, repite")

def get_selection_category(categories):
    category = random.choice(categories)

    while category.text == "Configurador de PCs":
        category = random.choice(categories)

    return category

#funcion que obtiene el producto y sus atributos
def get_ramdom_product_atributte(session, selected_category):
    product_page = session.get(selected_category.attr["href"])
    products = product_page.html.find(".c-product-card__wrapper")
    product = random.choice(products)
    image_src = product.find(".c-product-card__image", first=True).attrs["src"]
    product_name = product.find(".c-product-card__title", first=True).text
    product_price = product.find(".c-product-card__prices-actual", first=True).text
    final_price = product_price.replace(" €", "").replace(",", ".")
    return image_src, product_name, final_price

#Funcion que enseña la imagen del producto
def show_image(session, image_src):
    img_downloaded = session.get("https:" + image_src)
    image = Image.open(BytesIO(img_downloaded.content))
    image.show()

#Funcion que calcula los puntos de la ronda
def calculate_points(player1_gess, player2_gess, final_price):
    player1_points = player1_gess - final_price
    player2_points = player2_gess - final_price

    if player1_points < 0:
        player1_points = player1_points * -1

    if player2_points < 0:
        player2_points = player2_points * -1

    return player1_points, player2_points

#Funcion que calcula el ganador
def check_winner(player1_points_final, player2_points_final):
    if player1_points_final < player2_points_final:
        ganador = "Jugador 1"
    else:
        ganador = "Jugador 2"
    return ganador


def main():
    session = HTMLSession()

    print("Bienvenidos al precio justo, vamos a intentar adivinar algunos precios")
    speak("Bienvenidos al precio justo, vamos a intentar adivinar algunos precios")

    round = 5
    player1_points_final = 0
    player2_points_final = 0

    while round >0:
        categories = get_pccom_categories(session)

        category1 = get_selection_category(categories)
        category2 = get_selection_category(categories)
        category3 = get_selection_category(categories)
        category4 = get_selection_category(categories)
        category5 = get_selection_category(categories)

        if round % 2 == 0:
            print("Jugador1 seleccione entre las siguientes categorias")
            speak("Jugador1 seleccione entre las siguientes categorias")

        else:
            print("Jugador2 seleccione entre las siguientes categorias")
            speak("Jugador2 seleccione entre las siguientes categorias")

        print("{}, {}, {}, {}, {}".format(category1, category2, category3, category4, category5))
        speak("{}, {}, {}, {}, {}".format(category1, category2, category3, category4, category5))

        selected_category = get_selected_category(category1, category2, category3, category4, category5)

        image_src, product_name, final_price = get_ramdom_product_atributte(session, selected_category)
        show_image(session, image_src)

        print(product_name)
        speak("EL nombre del producto es {}".format(product_name))

        print("Jugador 1, cuanto crees que vale?")
        speak("Jugador 1, cuanto crees que vale?")
        player1_gess = hear_price_and_get_num()

        print("Jugador 2, cuanto crees que vale?")
        speak("Jugador 2, cuanto crees que vale? ")
        player2_gess = hear_price_and_get_num()

        player1_points, player2_points = calculate_points(player1_gess, player2_gess, final_price)

        print("El precio era {}".format(final_price))
        speak("El precio era {}".format(final_price))

        print("Jugador 1, sumas {} a tu marcador".format(player1_points))
        speak("Jugador 1, sumas {} a tu marcador".format(player1_points))
        print("Jugador 2, sumas {} a tu marcador".format(player2_points))
        speak("Jugador 2, sumas {} a tu marcador".format(player2_points))

        player1_points_final = player1_points_final + player1_points
        player2_points_final = player2_points_final + player2_points

        if round == 5:
            print("Jugador 1, tienes acumulados {} en tu marcador".format(player1_points_final))
            speak("Jugador 1, tienes acumulados {} en tu marcador".format(player1_points_final))
            print("Jugador 2, tienes acumulados {} en tu marcadorr".format(player2_points_final))
            speak("Jugador 2, tienes acumulados {} en tu marcador".format(player2_points_final))

        round = round - 1

    ganador = check_winner(player1_points_final, player2_points_final)
    speak("Se termino el juego y el ganador es el {}".format(ganador))


if __name__ == "__main__":
    main()