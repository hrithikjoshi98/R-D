import random
import urllib.parse
# import requests
from curl_cffi import requests
import json
from fake_useragent import UserAgent

ua = UserAgent()
cookies = {
    'dvid': 'c39e6874-ae2a-468b-ad1a-bdd5a41c067d',
    'brc_cabs_ab': '',
    'bm_sz': '89AC0EAD62B5D7509EA75552834CEA99~YAAQFFM2F1PhxKqTAQAAgpl1PxpepyhB1PV0G7xU6qmcWn4JHAoXiP+vfcllvrMdL6mF9XJUkjWdBIp3JygyOb1dIOXAbywbrOLb3xb75KHrb9O4IriorheShmrGuUi/DeDaH90zyhwUFphBJ4mlxbjZrCrd9CPr7DvaD4A8/W/82GlKiS8872UnWwlh6CsJJQpO0DwcfzSiiAxkMOVimnPBb8ounIFYNhAolbP0GxK37YkO2PrCDXh4Kd0yAlDwnjCAZwLuFNAUdmawnBKNxaj5gX0YK6hJ44R6PJGaHGE4Yya10v3ddCdZCmh5kO0CXy6CnAUum8hOT5TR5X8MgzHJjnJfSg5bSktzx3xRgFX4ZBQWavZ4jdzbDenZwpk053sUeFaF+ClBKfGKUGFGA9le~3159605~4408376',
    'AMCVS_1E0D22CE527845790A490D4D%40AdobeOrg': '1',
    's_ecid': 'MCMID%7C35180419887856374372291499899633882820',
    '_abck': 'E122D893CEEA624513D06C55CC081557~0~YAAQFFM2F1/hxKqTAQAAV5x1Pw317zUOdL5TEys7vXPsWGg7PuuOAPclwR7cX2auN5Jce2LCebXRUOtkB+X/sn7IYF4IVoY8ip2xl+wlDRw/QhRoivT4yZbVNQ46fjSFJwZHbF0f3+ZMgD0gVJrs0utT0tcudD04u3uTR26f+BU3HRvxMwdmsSEo2sBaDisqxABNGd543LSOFib9fmw6JWUMhzS1ppfpXDWRbfYJkY9PjV6nz/v/x2zIef54RB0lLhIP9qO/4drf4lK8uEq+wgxocm0b3vsDkFS6i5pjNiOyqS5g81TXT1Dqx4A+amQtixnpsCvTymKeySkk0dUfUHiJ8I40s7qN7t2tGEvSPH6PFAIG8g4ICcNRnTNDsPXKBOUKI4YbmwbEITs5hw4eF8RlsqX6qt3rux1aSY9W6noMlisOMqq1kv7785zbidIg1v4Gguk+CVglccew0p0aaa4xGFrUPDkfbqqPxIGJ0G4UZ3TT~-1~||0||~-1',
    'AMCV_1E0D22CE527845790A490D4D%40AdobeOrg': '1099438348%7CMCIDTS%7C20096%7CMCMID%7C35180419887856374372291499899633882820%7CMCAAMLH-1736836259%7C12%7CMCAAMB-1736836259%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1736238659s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.1.0',
    '_fbp': 'fb.1.1736231460243.789146887523561254',
    '_gcl_au': '1.1.1719554786.1736231460',
    'ak_bmsc': '50BECC795BA65F3B57F00A9E545ABFDC~000000000000000000000000000000~YAAQFFM2F3nhxKqTAQAAJZ91Pxp9wYbpmLh/uYy1Vhl4cctpfW/58yqH7D1VCSb2awyjL6UbxEv66HkuV3PKaSnLJU0anlNL7HOh+IN0VweDl4GdIYxR5KpwbZ7VSQhHS+wsK4k0UvXV4DiTkCv1ck+MdFi3K7ixjWStUZ24aCAt40Pn+S5b7WzuPmbF/J5l8NVoO2tTKHXwGXFDZdEPIUhaR9szEGGAMvINRem9qRteG5CuKG2UBN0cISTtdlcKkdsOAFQ0Qf5GyIe0N1bSjcOfo3X6KpKXAu/2wRz1C+9UTKYomOk99tfmXEOYtDdqTl2oEjb4MvYJnOewD2t0WRwNGJHSs3p9WKGEbnns0r4azUUSlp7XHvBLoNwktSXeyuvLHF6a0/mZcU5Wt3a34zlKzZVND3nhokju/FJP/HaaRXSDtOuKc6Ds125lwrRaFxuyuRerbfhh30ftUjrS3A==',
    'bm_sv': 'D56D0CCE3B6E436AB25285E9C0E73C1F~YAAQFFM2F5fjxKqTAQAAT+J1PxqzfJa9fCHeh3FNqep/SVZK/2bvTYZXtqR6G7BYj4pffMKQh8mH+g4xQQsqfqZW3LBKan5uBaELGbSYwGqubwjnaESJO7tMd7R7QgWCg6EYet4Qixnzz8Q3K+9Sx6Dr+NAdVgkrQ2tCkR+W7aZmJCCfmNS/rPc9ttLw6PwTV07C3JcLGSLcuhyncSSe4Xtv6XI94BWtU4p2UfajlzSmz9k/CK4ube4Sx7txOdb+gn4l9/o=~1',
    's_pers': '%20s_depth%3D1%7C1736233263468%3B%20s_vnum%3D1738348200474%2526vn%253D1%7C1738348200474%3B%20s_lv%3D1736231495673%7C1830839495673%3B%20s_lv_s%3DFirst%2520Visit%7C1736233295673%3B%20gpv_pn%3Dfunnel%253Adomestic%2520cabs%253Alisting%7C1736233295676%3B%20s_invisit%3Dtrue%7C1736233295677%3B%20s_nr3650%3D1736231495678-New%7C2051591495678%3B%20s_nr30%3D1736231495678-New%7C1738823495678%3B%20s_nr120%3D1736231495679-New%7C1746599495679%3B%20s_nr7%3D1736231495679-New%7C1736836295679%3B',
    's_sess': '%20s_cc%3Dtrue%3B%20tp%3D2537%3B%20s_ppv%3Dfunnel%25253Adomestic%252520cabs%25253Alisting%252C30%252C22%252C759%3B%20s_sq%3D%3B',
}


json_data = {
    'preApplyCouponCode': None,
    'departure_date': '09-01-2025',
    'return_date': None,
    'trip_type': 'AT',
    'pickup_time': '10:00',
    'drop_time': None,
    'source_location': {
        'airport': True,
        'address': 'Ahmedabad International Airport, airport, Ahmedabad, Gujarat, India',
        # 'latitude': 23.0716999,
        # 'longitude': 72.61995999999999,
        'pincode': '382405',
        'place_id': 'ChIJ384AuyiBXjkR656MJ9Yuk5U',
        'is_city': False,
        'city': 'Ahmedabad',
        'city_code': None,
        'google_city': 'Ahmedabad',
        'state': 'Gujarat',
        'is_airport': True,
        'main_text': None,
        'mainText': None,
        'secondary_text': None,
        'country': 'India',
        'country_code': 'IN',
    },
    'destination_location': {
        'city': 'Surat',
        'stn': 'Surat Airport',
        'id': 'GhIJwr8IGjMdNUARzhsnhXkvUkA',
        'is_airport': True,
        'is_city': False,
        'address': 'Surat Airport',
        # 'latitude': 21.114061,
        # 'longitude': 72.741792,
        'pincode': None,
        'place_id': 'GhIJwr8IGjMdNUARzhsnhXkvUkA',
        'google_city': 'Surat',
        'state': 'Gujarat',
        'country': 'India',
        'country_code': 'IN',
    },
    'source_city': None,
    'destination_city': None,
    'booking_device': 'desktop',
    'package_key': None,
    'fetch_package_list': False,
    'airport_cabs_enabled': True,
    'hr_cabs_enabled': True,
    'book_mode': 'D',
    'at_cross_sell_request': False,
    'profile_type': 'PERSONAL',
    'session_token': '',
    'email': '',
    'is_e_pass_enabled': True,
    'is_custom_payment_allowed': True,
    'is_default_search': True,
    'connector_search': False,
    'show_kit_enabled_cabs': True,
    'is_intercity_2': True,
    'rating_show': True,
    'mybiz_traveller_email': None,
    'mybiz_traveller_type': None,
    'is_other_cabs_enabled': True,
    'pokus_flags': [
        {
            'key': 'OS_Listing_Packages',
            'flag': True,
        },
        {
            'key': 'Listing_Part_Payment',
            'flag': False,
        },
        {
            'key': 'Listing_Assisted_Widget_web',
            'flag': False,
        },
        {
            'key': 'review_assisted_widget_dweb',
            'flag': True,
        },
        {
            'key': 'Mybiz_Assured_Cab_dweb',
            'flag': True,
        },
    ],
    'fetch_ryd_cabs': True,
    'funnel_source': None,
    'ih_flow': False,
    'stopovers': [],
}


token = "aa48e53ef4934d95a56acecacaec8fe454ebf634a98"


browsers = [
    'chrome99',
    'chrome100',
    'chrome101',
    'chrome104',
    'chrome107',
    'chrome110',
    'edge99',
    'edge101',
]

for atampt in range(1, 50):
    url = 'https://cabs.makemytrip.com/desktop/searchV2'

    # not working
    # proxy = 'http://scraperapi:03a620dbdc81e9e5c772a86859eb777a@proxy-server.scraperapi.com:8001'
    # proxy = "http://9dbe950ef6284a5da9e7749db9f7cbd1:@api.zyte.com:8011/"
    # proxies = {
    #     'proxy': {
    #         'http': proxy,
    #         'https': proxy,  # Use the same proxy for HTTPS
    #     }
    # }

    # not working
    # random_number = random.randint(10000000, 99999999)
    # username = f'actowiz-stc-US'
    # # username = f'actowiz-res-US-any-sid-{random_number}'
    # password = 'yYNSa0hbTdfNUIh'
    # server = 'gw.ntnt.io'
    # port = '5959'
    # proxies = {
    #     'http': f'http://{username}:{password}@{server}:{port}',
    #     # 'https': f'http://{username}:{password}@{server}:{port}'
    # }

    # random_user_agent = ua.random
    # print(f"Random User-Agent: {random_user_agent}")


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

    # response = requests.get(
    #     'https://httpbin.org/ip',
    #     proxies=proxies
    # )


    # target_url = f'https://us.shein.com/bff-api/product/get_goods_detail_realtime_data?_ver=1.1.8&_lang=en&goods_id={pid}&mallCode=1&isUserSelectedMallCode=1'
    # encoded_query_url = urllib.parse.quote(url, safe='')
    # todo - sending req using proxy (Scrape Do)
    # url = f'''http://api.scrape.do?token={token}&url={encoded_query_url}&super=true'''
    # url = f'''http://api.scrape.do?token={token}&url={target_url}&super=true'''


    # Randomly select a browser from the list
    selected_browser = random.choice(browsers)
    # Impersonate the selected browser
    # requests.impersonate(selected_browser)

    response = requests.post(
        url,
        headers=headers,
        json=json_data,
        impersonate=selected_browser
    )

    print('headers', response.headers)

    try:
        json_d = json.loads(response.text)
        print(response.text)
        print(atampt, response.status_code)
        cab_list = json_d['response']['cab_list']
        for i in cab_list:
            price = i['fare_details']['display_properties'][0]['Base Fare']
            print(price)
    except Exception as e:
        print('Error to get cabs')


    print('\n\n')

# with cookie
# 3563
# 3637
# 4651
# 8493
# 9793
# 14500
# 16820

# without cookie
# 3563
# 3637
# 4651
# 8493
# 9793
# 14500
# 16820
















