import os
import time
# import pyperclip
from pywinauto import Application, Desktop
import pandas as pd
import time
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options



# host = '185.124.241.137'
# host = '185.124.241.199'
# host = '185.124.241.109'
# host = '185.124.241.42'
host = '185.124.241.192'

port = '12323'
user = '14a148fa21239'
passw = 'ceae0888a2'


proxy = f'https://{user}:{passw}@{host}:{port}'

wire = {
    'http': proxy,
    'https': proxy
}

# Proxy details (Replace these with your actual proxy details)
# proxy = "http://proxy.example.com:8080"  # Replace with your proxy address and port

# Set up Chrome options to use the proxy
chrome_options = Options()
# chrome_options.add_argument(f'--proxy-server={proxy}')  # Set the proxy server

# Path to ChromeDriver (Download the correct version from https://sites.google.com/chromium.org/driver/)
chrome_driver_path = 'C:\\path\\to\\chromedriver.exe'  # Replace with your path to chromedriver.exe

# Start Chrome with the specified options
driver = webdriver.Chrome(seleniumwire_options=wire, options=chrome_options)

# Give Chrome some time to start
time.sleep(5)

# Now, connect to the Chrome window using pywinauto
app = Application(backend="uia").connect(title_re=".*Google Chrome.*")

# Get the window for the new tab
window = app.window(title_re=".*Google Chrome.*")

# URL to visit
url = 'https://us.shein.com/1pc-Cute-Computer-Keyboard-Wrist-Rest-Mouse-Pad-With-Hand-Pillow-Anti-Friction-Warmth-And-Ergonomic-Design-For-Office-Desk-p-32351743.html'

# Read URLs from CSV
df = pd.read_csv('shein-2024-12-27.csv')
urls = df['link']

# Find the address bar
address_bar = window.child_window(title="Address and search bar", control_type="Edit")

# Set the first URL in the address bar and press Enter
address_bar.set_text(url)
address_bar.type_keys("{ENTER}", with_spaces=True)
time.sleep(5)

# Flag for switching window titles
flag = False

# Loop through URLs and interact with the address bar
for pos, url in enumerate(urls[:10]):
    try:
        # If it's not the first iteration, re-find the address bar after page load
        if flag:
            window = app.window(title_re=".*Google Chrome.*")
            address_bar = window.child_window(title="Address and search bar", control_type="Edit")
            address_bar.wait('ready', timeout=10)  # Wait for the address bar to be ready

        # Set the new URL and press Enter
        address_bar.set_text(url)
        address_bar.type_keys("{ENTER}", with_spaces=True)

        # Wait for the page to load before continuing
        time.sleep(5)

    except Exception as e:
        # In case of any error (e.g., address bar not found), print and continue
        print(f"Error interacting with address bar for URL {url}: {e}")

    # Set flag to True for the next iteration
    flag = True
    time.sleep(60)

# Quit the WebDriver instance after finishing the automation
driver.quit()



