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


def set_cookies(driver, cookies_path):
    try:

        with open("cookies.json", "r") as file:
            cookies = json.load(file)

        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.refresh()

    except FileNotFoundError:
        print("Le fichier de cookies n'a pas été trouvé. 2 min avant la creation du fichier cookies...")
        time.sleep(120)
        cookies = driver.get_cookies()
        pickle.dump(cookies, open(cookies_path, "wb"))

    time.sleep(5)



base_path = r"C:\Users\adrien\Desktop\ADRIEN\python\MusicEsound".replace(os.sep, '/')


chromedriver_path = chromedriver_autoinstaller.install()

options = selenium.webdriver.ChromeOptions()
options.add_argument("--disable-search-engine-choice-screen")
options.add_argument("--incognito")


driver1 = uc.Chrome(options, driver_executable_path=chromedriver_path, headless=False)
driver1.set_page_load_timeout(300)
driver1.maximize_window()

driver1.get('https://listen.esound.app/')
set_cookies(driver1, f"{base_path}/Cookies/www.esound_cookies.pkl")

time.sleep(300)