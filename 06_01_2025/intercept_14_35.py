import os
import threading
from mitmproxy import http
import json
import socket

def response(flow: http.HTTPFlow):

    if ".html" in flow.request.pretty_url:
        print(f"Request URL: {flow.request.pretty_url}")
        print(f"Response Status Code: {flow.response.status_code}")
        print(f"Response Headers: {flow.response.headers}")
        # print(f"Response Body: {flow.response.text[:500]}")
        if flow.response.status_code == 404:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('localhost', 65432))
                s.sendall(b"response received")

    if "get_goods_detail_realtime_data" in flow.request.pretty_url:
        print(f"Request URL: {flow.request.pretty_url}")
        print(f"Response Status Code: {flow.response.status_code}")
        print(f"Response Headers: {flow.response.headers}")
        # print(f"Response Body: {flow.response.text[:500]}")
        if flow.response.status_code == 200:
            json_data = json.loads(flow.response.text)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('localhost', 65432))
                s.sendall(b"response received")

            sku_id = json_data['info']['productInfo']['goods_sn']
            path = r'C:\hrithik\Research and Analysis Wing\requests\m_shein_com\files'
            os.makedirs(path, exist_ok=True)
            with open(f'{path}\\{sku_id}.html', 'w', encoding='utf-8') as file:
                file.write(json.dumps(json_data, indent=4))


        # mitmdump -s intercept.py


