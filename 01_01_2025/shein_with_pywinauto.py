import os
import time
# import pyperclip
from pywinauto.keyboard import send_keys
from pywinauto import Application, Desktop
import pandas as pd
from mitmproxy import http


def is_page_loading(browser_window):
    loading_indicator = browser_window.child_window(title="Loading", control_type="ProgressBar")  # Update the title based on the browser
    return loading_indicator.exists()

def response(flow: http.HTTPFlow):
    # Intercept a specific URL
    if "specific_keyword" in flow.request.pretty_url:
        print(f"Request URL: {flow.request.pretty_url}")
        print(f"Response Status Code: {flow.response.status_code}")
        print(f"Response Headers: {flow.response.headers}")
        print(f"Response Body: {flow.response.text[:500]}")


def page_save_code(window, actual_path):
    window.type_keys("^s", with_spaces=True)

    desktop = Desktop(backend="win32")
    save_as_dialog = desktop.window(title_re=".*Save As.*")

    for child in save_as_dialog.descendants():
        print(child.control_type, child.class_name())
        if "Edit" in str(child.control_type):# or "ComboBox" in str(child.control_type):
            # address_bar = child
            address_bar = window.child_window(control_type=child.control_type)

            print(f"Found address bar: {address_bar}")
            break  # Stop the loop once we find the control

    # Wait for the page to load
    timeout = 30  # seconds
    start_time = time.time()
    while time.time() - start_time < timeout:
        if not is_page_loading(window):
            print("Page loaded successfully!")
            break
        time.sleep(1)
    else:
        print("Timeout: Page did not load completely.")

    if address_bar:
        address_bar.click_input()  # Focus on the ComboBox (Address Bar)
        send_keys('^a')
        # Copying text (Ctrl + C)
        send_keys(actual_path + f'\shein_uk_{pos + 1}')  # Simulates pressing Ctrl + C to copy

        # Simulate a delay to ensure the text is copied before pasting
        # You can adjust the sleep time as needed

        time.sleep(0.5)

        # Pasting text (Ctrl + V)
        send_keys('^v')  # Simulates pressing Ctrl + V to paste
    else:
        print("Address bar not found.")

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
for pos, url in enumerate(urls[:1000]):
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
        time.sleep(5)

        # page_save_code(window, actual_path)

        print('----------')
    except Exception as e:
        # In case of any error (e.g., address bar not found), print and continue
        print(f"Error interacting with address bar for URL {url}: {e}")

    # Set flag to True for the next iteration
    flag = True


