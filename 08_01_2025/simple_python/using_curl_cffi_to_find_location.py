import json
import requests


headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,tr;q=0.8',
        # 'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://cabs.makemytrip.com',
        # 'pragma': 'no-cache',
        # 'priority': 'u=1, i',
        'referer': 'https://cabs.makemytrip.com/',
        # 'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': '"Windows"',
        # 'sec-fetch-dest': 'empty',
        # 'sec-fetch-mode': 'cors',
        # 'sec-fetch-site': 'same-origin',
        # 'traceparent': '00-dc01b70f952c01e6796f7d0e8b7b6156-bc36ebf99077cf96-01',
        # 'user-agent': random_user_agent,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }


# query = 'Surat station, Railway Station Circle, Railway Station Area, Varachha, Surat, Gujarat, India'
query = 'Ahmedabad Railway Station, Kalupur Railway Station Road, Sakar Bazzar, Kalupur, Ahmedabad, Gujarat, India'

params = {
    'query': query,
    'tripType': 'OW',
    'requestFor': 'from',
    # 'selectedLat': '23.0716999',
    # 'selectedLng': '72.61995999999999',
    'isCorporate': 'false',
    'countryCode': 'IN',
}

# from
# Surat station, Railway Station Circle, Railway Station Area, Varachha, Surat, Gujarat, India

# to
# Ahmedabad Railway Station, Kalupur Railway Station Road, Sakar Bazzar, Kalupur, Ahmedabad, Gujarat, India

response = requests.get('https://cabs.makemytrip.com/autocomplete/v3', params=params, headers=headers)


print(response.text)
print(response.status_code)

json_data = json.loads(response.text)

address = json_data['res'][0]['structured_formatting']['secondary_text']


















