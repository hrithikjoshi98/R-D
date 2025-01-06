import os
import time
# import pyperclip
from pywinauto import Application, Desktop



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

address_bar = window.child_window(title="Address and search bar", control_type="Edit")

address_bar.set_text(url)

# Simulate pressing 'Enter'
address_bar.type_keys("{ENTER}", with_spaces=True)


