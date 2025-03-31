from requests_html import HTMLSession
import time
from selenium import webdriver
from selenium.common import NoSuchElementException

SESSION = HTMLSession()
EMAIL = "sergio@gmail.com"
PWD = "password"

def check_pccom ():
    URL_PCCOM = "https://www.pccomponentes.com/asus-dual-geforce-rtx-4060-v2-oc-edition-8gb-gddr6-dlss3"
    s_pccom = SESSION.get(URL_PCCOM)
    buy_zone = s_pccom.html.find("#btnsWishAddBuy")
    if len(buy_zone) > 0:
        driver = webdriver.firefox()
        driver.get(URL_PCCOM)
        driver.find_element_by_class_name("confirm").click()
        driver.find_element_by_class_name("accept").click()
        driver.find_element_by_class_name("button-buy").click()
        time.sleep(1)
        driver.find_element_by_class_name("confirm").click()
        driver.find_element_by_class_name("button-buy").click()

        is_form_loaded = False
        form = None

        while not is_form_loaded:
            try:
                form = driver.find_element_by_class_name("login100-form").click()
            except NoSuchElementException:
                print("No funciona el formulario")
        email = form.find_element_by_name("jform[email]")
        password = form.find_element_by_name("jform[password]")

        email.send_keys(EMAIL)
        password.send_keys(PWD)
        driver.find_element_by_class_name("login100-form-btn").click()
    else:
        print("nada en PCOM")


def check_coolm():
    URL_COOLM = "https://www.coolmod.com/msi-geforce-rtx-4070-ventus-3x-e1-12g-oc-12gb-gddr6/"
    s_coolm = SESSION.get(URL_COOLM)
    found = s_coolm.html.find("main-buy")
    if len(found) > 0:
        driver = webdriver.firefox()
        driver.get(URL_COOLM)
        driver.find_element_by_class_name("confirm").click()
        driver.find_element_by_class_name("accept").click()
        driver.find_element_by_class_name("button-buy").click()
        time.sleep(1)
        driver.find_element_by_class_name("confirm").click()
        driver.find_element_by_class_name("button-buy").click()

        is_form_loaded = False
        form = None

        while not is_form_loaded:
            try:
                form = driver.find_element_by_class_name("login100-form").click()
            except NoSuchElementException:
                print("No funciona el formulario")
        email = form.find_element_by_name("jform[email]")
        password = form.find_element_by_name("jform[password]")

        email.send_keys(EMAIL)
        password.send_keys(PWD)
        driver.find_element_by_class_name("login100-form-btn").click()
    else:
        print("nada en COLLMOD")
        


def main():

    while True:
        check_pccom()
        check_coolm()
        time.sleep(30)


if __name__ == "__main__":
    main()