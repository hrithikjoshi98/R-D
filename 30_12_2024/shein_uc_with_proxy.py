import time
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver
# from seleniumbase import webdriver
# from selenium import webdriver
import undetected_chromedriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


def block_assets(driver):
    driver.execute_cdp_cmd("Network.enable", {})  # Enable Network monitoring
    driver.execute_cdp_cmd(
        "Network.setBlockedURLs",
        {
            "urls": [
                "*.css",  # Block CSS files
                "*.webp",  # Block WEBP images
                "*.woff2",  # Block WOFF2 fonts
                "*.png",
                "*.jpg",
                "*.jpeg",
                "*.svg"
            ]
        },
    )

def create_session1(main_url, proxy):
    # options = webdriver.ChromeOptions()
    options = Options()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    options.add_argument('--user-agent=' + user_agent)
    options.add_argument("--start-maximized")  # Start the browser maximized
    options.add_argument("--incognito")  # Open in incognito mode
    options.add_argument("--disable-extensions")  # Disable browser extensions
    # options.add_argument("--no-sandbox")  # Useful for Linux environments
    options.add_argument("--disable-dev-shm-usage")
    driver = undetected_chromedriver.Chrome(options=options)
    driver.get(main_url)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    return driver


# Proxy details
# host = '185.124.241.137'
# host = '185.124.241.199'
# host = '185.124.241.109'
# host = '185.124.241.42'
host = '185.124.241.192'

port = '12323'
user = '14a148fa21239'
passw = 'ceae0888a2'


proxy = f'https://{user}:{passw}@{host}:{port}'
url = 'https://us.shein.com/1pc-Cute-Computer-Keyboard-Wrist-Rest-Mouse-Pad-With-Hand-Pillow-Anti-Friction-Warmth-And-Ergonomic-Design-For-Office-Desk-p-32351743.html?src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_14%60ps%3D2_14%60jc%3DitemPicking_017172971&src_module=all&src_tab_page_id=page_home1735536383063&mallCode=1&pageListType=4'

df = pd.read_csv('shein-2024-12-27.csv')
urls = df['link']
driver = create_session1(url, proxy)

val = input('press any key :')

for pos, i in enumerate(urls):

    # time.sleep(10)
    # driver = create_session2(i)
    driver.get(i)
    try:
        selector = '//h1[contains(@class,"product-intro__head-name")]'
        title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, selector))).text
    except:
        title = ''
    print('Position :', pos + 1, '-', title, '\n')

time.sleep(10)
driver.quit()


















