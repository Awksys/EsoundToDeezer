import time
import chromedriver_autoinstaller
import pickle
import os
import json

import selenium.webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import random
import re


def set_cookies(driver, cookies_path):
    try:

        with open(cookies_path, "rb") as file:
            cookies = pickle.load(file)

        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.refresh()

    except FileNotFoundError:
        print("Le fichier de cookies n'a pas été trouvé. 2 min avant la creation du fichier cookies...")
        time.sleep(120)
        cookies = driver.get_cookies()
        pickle.dump(cookies, open(cookies_path, "wb"))

    time.sleep(5)


def is_in_page_player(element):
    while element:
        if element.get_attribute('id') == 'page_player':
            return True
        if element.tag_name == 'html':
            break
        try:
            element = element.find_element(By.XPATH, '..')
        except NoSuchElementException:
            break
    return False


def get_popularity():
    try:
        popularite_element = WebDriverWait(driver1, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@aria-label, "Popularité")]'))
        )

        aria_label = popularite_element.get_attribute("aria-label")

        print(aria_label)

        match = re.search(r"Popularité\s*[:]\s*(\d+\.\d+)", aria_label)

        if match:
            popularity_value = float(match.group(1))
            print(f"Valeur de la popularité : {popularity_value}")
        else:
            popularity_value = None
            print("Impossible d'extraire la valeur de la popularité")

        return popularity_value

    except Exception as e:
        print(f"Erreur : {e}")


def safe_click(driver, locator):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        element.click()
    except StaleElementReferenceException:
        print("⚠️ Élément obsolète, nouvelle tentative...")
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        element.click()

def try_to_like(search_str, min_pop):
    search_input.clear() 
    search_input.send_keys(search_str)
    time.sleep(1)

    try:
        like_button = WebDriverWait(driver1, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label*="Coups de cœur"]'))
        )
        
        time.sleep(1)

        if is_in_page_player(like_button):
            return False

        print("ok")
        popularity = get_popularity()

        if not popularity or popularity < min_pop:
            return False
        
        aria_label = like_button.get_attribute("aria-label")
        
        if "Ajouter" in aria_label:
            like_button.click()
            print("✅ Le bouton 'Ajouter aux Coups de cœur' a été cliqué !")
        else:
            print("❌ Déjà liké")
        
        time.sleep(random.randint(4,5))
        return True
        
    except Exception as e:
        print(f"⚠️ Une erreur est survenue : {e}")


base_path = r"C:\Users\adrien\Desktop\ADRIEN\python\MusicEsound".replace(os.sep, '/')

with open("music_file_2.json", "r", encoding="utf-8") as file:
    all_music = json.load(file)

not_found_music = []
doubt_music = []


chromedriver_path = chromedriver_autoinstaller.install()

options = selenium.webdriver.ChromeOptions()
options.add_argument("--disable-search-engine-choice-screen")


driver1 = uc.Chrome(options, driver_executable_path=chromedriver_path, headless=False)
driver1.set_page_load_timeout(300)
driver1.maximize_window()

driver1.get('https://www.deezer.com/fr/channels/explore/explore-tab')
set_cookies(driver1, f"{base_path}/Cookies/deezer_cookies.pkl")

time.sleep(1)


ActionChains(driver1).send_keys(Keys.ESCAPE).perform()


search_input = driver1.find_element(By.CSS_SELECTOR, "input[type='search']")


#all_music = []

start_len = len(all_music)

for i in range(start_len):

    last_music = all_music.pop()

    title = last_music["titre"]

    if title.lower().startswith("new"):
        title = title[4:].strip()
    
    title = title.lower().replace(" x ", "").strip()

    print("Tentative", i+1 , "/", start_len, ":", title + " " + last_music["artiste"])
    
    if try_to_like(title + " " + last_music["artiste"], 1):
        continue

    doubt_music.append(last_music)
    
    if len(title.split()) > 2:
        if try_to_like(title, 2):
            continue

    search_words = title.split()

    while len(search_words) > 2:
        search_words.pop()
        search = " ".join(search_words)

        if try_to_like(search, 2):
            break

    if len(search_words) > 1:
        continue


    print(last_music["titre"] + " de " + last_music["artiste"] + " n'a pas été trouvée")

    not_found_music.append(last_music)



with open("not_found_music.json", "w", encoding="utf-8") as file:
    json.dump(not_found_music, file, indent=4, ensure_ascii=False)

with open("doubt_music.json", "w", encoding="utf-8") as file:
    json.dump(doubt_music, file, indent=4, ensure_ascii=False)


time.sleep(100000000)