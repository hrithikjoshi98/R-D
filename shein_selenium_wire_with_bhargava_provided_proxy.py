import time
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

# Proxy details
# host = '185.124.241.137'
# host = '185.124.241.199'
# host = '185.124.241.109'
# host = '185.124.241.42'
host = '185.124.241.192'

port = '12323'
user = '14a148fa21239'
passw = 'ceae0888a2'

block_requests = False

# https://us.shein.com/bff-api/product/get_goods_detail_realtime_data?_ver=1.1.8&_lang=en&goods_id=32351743&mallCode=1&isUserSelectedMallCode=1
def intercept_request(request):
    global block_requests
    # Block resources by condition
    # block_keywords = ['jpg', 'png', 'gif', 'css', 'woff', 'font']
    # block_keywords = ['gif', 'css', 'woff', 'font']
    # if any(keyword in request.url for keyword in block_keywords):
    #     request.abort()

    url_cra = 'https://us.shein.com/bff-api/product/get_goods_detail_realtime_data'

    url_cra_lis = ['https://us.shein.com/bff-api/product/get_goods_detail_realtime_data',
            'https://us.shein.com/api/productInfo/realTimeData/query',
                   'https://us.shein.com/api/productInfo/recommendGroup/query']

    block_keywords = ['jpg', 'png', 'gif', 'css', 'woff', 'webp', 'font']
    # Check if the request URL matches any of the target URLs
    if any(keyword in request.url for keyword in url_cra_lis):
        # Print or capture the request data
        print("Captured Request URL:", request.url)
        # print("Request Headers:", request.headers)
        if request.body:
            print("Request Body:", request.body.decode('utf-8'))
            block_requests = True

        if block_requests:
            request.abort()
    elif any(keyword in request.url for keyword in block_keywords):
        request.abort()
    else:
        # Block all other requests
        if block_requests:
            request.abort()
        else:
            pass


def get_visible_text_and_stop_loading():
    try:
        # Wait for partial page load
        # Retrieve all visible text content
        visible_text = driver.execute_script("""
            return Array.from(document.querySelectorAll('*'))
                .filter(el => el.offsetParent !== null)
                .map(el => el.innerText)
                .filter(txt => txt.trim().length > 0)
                .join('\\n');
        """)
        # Stop further loading
        # Stops page load
        return visible_text
    except Exception as e:
        print(f"Error while scraping: {e}")
        return ""


# Selenium Wire options
seleniumwire_options = {
    'proxy': {
        'http': f'http://{user}:{passw}@{host}:{port}',
        'https': f'https://{user}:{passw}@{host}:{port}',
        # Bypass proxy for specific hosts (optional)
        'no_proxy': 'localhost,127.0.0.1'
    }
}
optionss = webdriver.ChromeOptions()
optionss.add_argument("--disable-blink-features=AutomationControlled")
optionss.add_experimental_option("excludeSwitches", ["enable-automation"])
optionss.add_experimental_option('useAutomationExtension', False)
# optionss.add_argument("--blink-settings=imagesEnabled=false")  # Disable images
optionss.add_argument("--disable-gpu")
optionss.add_argument("--disk-cache-size=524288000")
driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options, options=optionss)
# driver = webdriver.Chrome(options=optionss)

# Test the proxy
# driver.get("https://m.shein.com/us/pdsearch/pants/")
# driver.get("https://m.shein.com/us/risk/challenge?captcha_type=905&redirection=https://m.shein.com%2Fus%2Fpdsearch%2Fpants%2F&risk-id=E2646305054931945472")
# driver.get("https://m.shein.com/us/risk/challenge?captcha_type=904&redirection=https://m.shein.com%2Fus%2Fpdsearch%2Fpants%2F&risk-id=E2646305054931945472")
# driver.get("https://m.shein.com/us/risk/challenge?captcha_type=903&redirection=https://m.shein.com%2Fus%2Fpdsearch%2Fpants%2F&risk-id=E2646305054931945472")
driver.get("https://us.shein.com/1pc-Cute-Computer-Keyboard-Wrist-Rest-Mouse-Pad-With-Hand-Pillow-Anti-Friction-Warmth-And-Ergonomic-Design-For-Office-Desk-p-32351743.html?src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_14%60ps%3D2_14%60jc%3DitemPicking_017172971&src_module=all&src_tab_page_id=page_home1735536383063&mallCode=1&pageListType=4")
val = input('Press any key :')

df = pd.read_csv('shein-2024-12-27.csv')
urls = df['link']

driver.request_interceptor = intercept_request
for pos, i in enumerate(urls):
    driver.get(i)
    try:
        # driver.request_interceptor = intercept_request
        # selector = '//h1[contains(@class,"product-intro__head-name")]'
        # title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, selector))).text
        # print('Position :', pos + 1, '-', title, '\n')
        time.sleep(5)
        # driver.execute_script("window.stop();")
        # scraped_text = get_visible_text_and_stop_loading()
        # print(f"Scraped Text from {i}:\n{scraped_text}\n")
    except:
        print('error')
    block_requests = False

time.sleep(100)
# Quit the browser
driver.quit()

