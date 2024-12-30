import time
from seleniumbase import SB, Driver
import os
import pandas as pd
from seleniumbase import Driver


# proxy = 'http://scraperapi:03a620dbdc81e9e5c772a86859eb777a@proxy-server.scraperapi.com:8001'
# proxy = 'http://9dbe950ef6284a5da9e7749db9f7cbd1:@api.zyte.com:8011/'
# proxy = 'https://api.scrape.do/?token=aa48e53ef4934d95a56acecacaec8fe454ebf634a98'
# host = '185.124.241.137'
# host = '185.124.241.199'
# host = '185.124.241.109'
host = '185.124.241.42'
# host = '185.124.241.192'

port = '12323'
user = '14a148fa21239'
passw = 'ceae0888a2'
# seleniumwire_options = {
#     'proxy': {
#         'http': f'http://{user}:{passw}@{host}:{port}',
#         'https': f'https://{user}:{passw}@{host}:{port}',
#         # Bypass proxy for specific hosts (optional)
#         'no_proxy': 'localhost,127.0.0.1'
#     }
# }

seleniumwire_options = f'{user}:{passw}@{host}:{port}'


with SB(uc=True, proxy=seleniumwire_options, incognito=True, wire=True, test=True, locale_code="en") as sb:
    # url = "https://us.shein.com/recommend/Shoes-and-Bags-sc-100123139.html"

    df = pd.read_csv('shein-2024-12-27.csv')
    urls = df['link']
    sb.activate_cdp_mode(urls[0])
    val = input('press any key :')
    for pos, i in enumerate(urls):

        # url = "https://httpbin.org/ip"
        url = i
        # sb.get(url)
        sb.cdp.get(url)
        try:
            selector = '//h1[contains(@class,"product-intro__head-name")]'
            title = sb.find_element(selector).text
            print('Position :', pos + 1, '-', title, '\n')
            sel = '//div[@class="product-intro__head-reviews"]//div[@class="common-rate"]'
            sb.find_element(sel)
        except Exception as e:
            print('error :', e)

        file_path = 'files'
        os.makedirs(file_path, exist_ok=True)
        with open(file_path + fr'\{str(pos)}' + '.html', 'w', encoding='utf-8') as save:
            save.write(sb.cdp.get_page_source())


# driver = Driver(wire=True, uc_cdp=True)
# try:
#     driver.proxy(seleniumwire_options)
#     driver.open("https://httpbin.io/ip")
#     driver.sleep(6)
# finally:
#     driver.quit()


