import random
import time
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

seleniumwire_options = {}

# iproyal proxy
# # host = '185.124.241.137'
# # host = '185.124.241.199'
# # host = '185.124.241.109'
# port = '12323'
# user = '14a148fa21239'
# passw = 'ceae0888a2'
# seleniumwire_options = {
#     'proxy': {
#         'http': f'http://{user}:{passw}@{host}:{port}',
#         'https': f'https://{user}:{passw}@{host}:{port}',
#         # Bypass proxy for specific hosts (optional)
#         'no_proxy': 'localhost,127.0.0.1'
#     }
# }


# netner proxy
# random_number = random.randint(10000000, 99999999)
# username = f'actowiz-res-US-any-sid-{random_number}'
# password = 'yYNSa0hbTdfNUIh'
# server = 'gw.ntnt.io'
# port = '5959'
# seleniumwire_options = {
#     'http': f'http://{username}:{password}@{server}:{port}',
#     'https': f'http://{username}:{password}@{server}:{port}'
# }


# scraperapi proxy
# proxy = 'http://scraperapi:03a620dbdc81e9e5c772a86859eb777a@proxy-server.scraperapi.com:8001'
# seleniumwire_options = {
#     'proxy': {
#         'http': proxy,
#         'https': proxy,  # Use the same proxy for HTTPS
#     }
# }

# Create a new instance of the browser
driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options)

driver.get("https://httpbin.org/ip")

time.sleep(100)
driver.quit()

# o/p "origin": "205.233.201.222"
# o/p "origin": "88.209.245.149"
