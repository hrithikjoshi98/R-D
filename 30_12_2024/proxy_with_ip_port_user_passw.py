import time
from seleniumwire import webdriver

# Proxy details
# host = '185.124.241.137'
# host = '185.124.241.199'
host = '185.124.241.109'

port = '12323'
user = '14a148fa21239'
passw = 'ceae0888a2'


# Selenium Wire options
seleniumwire_options = {
    'proxy': {
        'http': f'http://{user}:{passw}@{host}:{port}',
        'https': f'https://{user}:{passw}@{host}:{port}',
        # Bypass proxy for specific hosts (optional)
        'no_proxy': 'localhost,127.0.0.1'
    }
}

# Create a new instance of the browser
driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options)

# Test the proxy
driver.get("https://httpbin.org/ip")

time.sleep(100)
# Quit the browser
driver.quit()

# o/p "origin": "185.124.241.137"
# o/p "origin": "185.124.241.199"
# o/p "origin": "185.124.241.109"
