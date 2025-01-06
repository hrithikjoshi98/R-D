import os
import time
from pywinauto import Application, Desktop
from pywinauto.keyboard import send_keys
import pandas as pd
import pyperclip

file_path = 'files'
os.makedirs(file_path, exist_ok=True)

# Read URLs from CSV
df = pd.read_csv('shein-2024-12-27.csv')
urls = df['link']


app = Application(backend="win32").start("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
time.sleep(2)

# Connect to Chrome window

# Debug: List all open windows to identify the correct title
# desktop = Application(backend="win32").connect(title_re="New Tab - Google Chrome")
# for win in desktop.windows():
#     print(win.window_text())

# Attempt to connect to Chrome
try:
    apps = Application(backend="uia").connect(title_re="New Tab - Google Chrome")
    window = apps.window(title_re=".*New Tab - Google Chrome.*")
except Exception as e:
    print("Error: Unable to find Chrome window. Check the title or increase the delay.")
    raise e

address_bar = None
for child in window.descendants():
    if "Address Band Root" in str(child.control_type):  # Adjust this condition if necessary
        address_bar = child
        break


flag = False
# Loop through URLs
for pos, url in enumerate(urls[:10]):
    pyperclip.copy(file_path) # Sends CTRL+L to focus on the address bar
    send_keys("^v")  # Paste the URL using Ctrl+V
    send_keys("{ENTER}")  # Wait for the page to load before opening the next URL

# Close Chrome after processing
try:
    window.close()
except Exception as e:
    print(f"Error closing Chrome window: {e}")
