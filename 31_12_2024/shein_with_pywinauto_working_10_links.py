import os
import time
# import pyperclip
from pywinauto import Application, Desktop
import pandas as pd


app = Application(backend="uia").start("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
time.sleep(5)
# windows = Desktop(backend="uia").windows()
# for w in windows:
#     print(w.window_text())

apps = Application(backend="uia").connect(title_re="New Tab - Google Chrome")
# print(apps.windows())

window = apps.window(title_re=".*New Tab - Google Chrome.*")

url = 'https://us.shein.com/1pc-Cute-Computer-Keyboard-Wrist-Rest-Mouse-Pad-With-Hand-Pillow-Anti-Friction-Warmth-And-Ergonomic-Design-For-Office-Desk-p-32351743.html?src_identifier=on%3DIMAGE_COMPONENT%60cn%3Dshopbycate%60hz%3DhotZone_14%60ps%3D2_14%60jc%3DitemPicking_017172971&src_module=all&src_tab_page_id=page_home1735536383063&mallCode=1&pageListType=4{ENTER}'
url = url.split('?')[0]
# Interact with the browser (e.g., click address bar)
# window.Edit.type_keys(url+'{ENTER}')

# Loop through URLs
df = pd.read_csv('shein-2024-12-27.csv')
urls = df['link']
address_bar = window.child_window(title="Address and search bar", control_type="Edit")

flag = False
address_bar.set_text(url)
# Simulate pressing 'Enter'
address_bar.type_keys("{ENTER}", with_spaces=True)
print('HJ')
# time.sleep(10)
for pos, url in enumerate(urls[:10]):
    try:
        # If it's not the first iteration, re-find the address bar after page load
        try:
            if flag:
                # Wait for the window to settle and the address bar to become accessible
                window = apps.window(title_re=".*Google Chrome.*")
                # Ensure the address bar is available before interacting with it
                address_bar = window.child_window(title="Address and search bar", control_type="Edit")
                address_bar.wait('ready', timeout=1)  # Wait for the address bar to be ready
                # Set the new URL and press Enter
                address_bar.set_text(url)
        except:
            if flag:
                # Wait for the window to settle and the address bar to become accessible
                window = apps.window(title_re=".*Google Chrome.*")
                # Ensure the address bar is available before interacting with it
                address_bar = window.child_window(title="Address and search bar", control_type="Edit")
                address_bar.wait('ready', timeout=1)  # Wait for the address bar to be ready
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


