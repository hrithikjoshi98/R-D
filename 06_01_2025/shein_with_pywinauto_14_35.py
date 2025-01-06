import os
import time
# import pyperclip
from pywinauto.keyboard import send_keys
from pywinauto import Application, Desktop
import pandas as pd
from mitmproxy import http
import threading
import socket


response_received_event = threading.Event()


def handle_network_signal():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 65432))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(1024)
                if data == b"response received":
                    response_received_event.set()


app = Application(backend="uia").start("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe --remote-debugging-port=9222 --proxy-server=http://127.0.0.1:8080")
time.sleep(5)
# windows = Desktop(backend="uia").windows()
# for w in windows:
#     print(w.window_text())

actual_path = r'C:\hrithik\Research and Analysis Wing\requests\m_shein_com\files'
file_path = 'files'
os.makedirs(file_path, exist_ok=True)


apps = Application(backend="uia").connect(title_re="New Tab - Google Chrome")
# print(apps.windows())

window = apps.window(title_re=".*Google Chrome.*")

# url = 'https://www.shein.co.uk/SHEIN-Frenchy-Women-Jeans-Thickened-Denim-p-11646238.html?src_identifier=st%3D5%60sc%3Djeans%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_home1735274531240&mallCode=1&pageListType=4'
url = 'https://www.shein.co.uk/SHEIN-Frenchy-Women-Jeans-Thickened-Denim-p-11646238.html?src_identifier=st%3D5%60sc%3Djeans%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_home1735274531240&mallCode=1&pageListType=4'
url = url.split('?')[0]
# Interact with the browser (e.g., click address bar)

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

threading.Thread(target=handle_network_signal, daemon=True).start()

for pos, url in enumerate(urls[:1000]):
    # product not found url
    # url = 'https://www.shein.co.uk/Forever-21-Women-s-Pockets-Flare-Casual-All-Match-Jeans-p-46193057.html?src_identifier=st%3D5%60sc%3Djeans%60sr%3D0%60ps%3D1&src_module=search&src_tab_page_id=page_home1735274531240&mallCode=1&pageListType=4'
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
        except Exception as e:
            print('Error :', e)

        address_bar.type_keys("{ENTER}", with_spaces=True)
        print('itaration :', pos+1)
        # Wait for the page to load before continuing
        response_received_event.wait()
        response_received_event.clear()

        # page_save_code(window, actual_path)

        print('----------')
    except Exception as e:
        # In case of any error (e.g., address bar not found), print and continue
        print(f"Error interacting with address bar for URL {url}: {e}")

    # Set flag to True for the next iteration
    flag = True


