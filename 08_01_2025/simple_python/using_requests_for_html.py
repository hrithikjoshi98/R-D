import requests

cookies = {
    'dvid': 'c39e6874-ae2a-468b-ad1a-bdd5a41c067d',
    'bm_sz': '89AC0EAD62B5D7509EA75552834CEA99~YAAQFFM2F1PhxKqTAQAAgpl1PxpepyhB1PV0G7xU6qmcWn4JHAoXiP+vfcllvrMdL6mF9XJUkjWdBIp3JygyOb1dIOXAbywbrOLb3xb75KHrb9O4IriorheShmrGuUi/DeDaH90zyhwUFphBJ4mlxbjZrCrd9CPr7DvaD4A8/W/82GlKiS8872UnWwlh6CsJJQpO0DwcfzSiiAxkMOVimnPBb8ounIFYNhAolbP0GxK37YkO2PrCDXh4Kd0yAlDwnjCAZwLuFNAUdmawnBKNxaj5gX0YK6hJ44R6PJGaHGE4Yya10v3ddCdZCmh5kO0CXy6CnAUum8hOT5TR5X8MgzHJjnJfSg5bSktzx3xRgFX4ZBQWavZ4jdzbDenZwpk053sUeFaF+ClBKfGKUGFGA9le~3159605~4408376',
    'AMCVS_1E0D22CE527845790A490D4D%40AdobeOrg': '1',
    's_ecid': 'MCMID%7C35180419887856374372291499899633882820',
    '_abck': 'E122D893CEEA624513D06C55CC081557~0~YAAQFFM2F1/hxKqTAQAAV5x1Pw317zUOdL5TEys7vXPsWGg7PuuOAPclwR7cX2auN5Jce2LCebXRUOtkB+X/sn7IYF4IVoY8ip2xl+wlDRw/QhRoivT4yZbVNQ46fjSFJwZHbF0f3+ZMgD0gVJrs0utT0tcudD04u3uTR26f+BU3HRvxMwdmsSEo2sBaDisqxABNGd543LSOFib9fmw6JWUMhzS1ppfpXDWRbfYJkY9PjV6nz/v/x2zIef54RB0lLhIP9qO/4drf4lK8uEq+wgxocm0b3vsDkFS6i5pjNiOyqS5g81TXT1Dqx4A+amQtixnpsCvTymKeySkk0dUfUHiJ8I40s7qN7t2tGEvSPH6PFAIG8g4ICcNRnTNDsPXKBOUKI4YbmwbEITs5hw4eF8RlsqX6qt3rux1aSY9W6noMlisOMqq1kv7785zbidIg1v4Gguk+CVglccew0p0aaa4xGFrUPDkfbqqPxIGJ0G4UZ3TT~-1~||0||~-1',
    'AMCV_1E0D22CE527845790A490D4D%40AdobeOrg': '1099438348%7CMCIDTS%7C20096%7CMCMID%7C35180419887856374372291499899633882820%7CMCAAMLH-1736836259%7C12%7CMCAAMB-1736836259%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1736238659s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.1.0',
    '_fbp': 'fb.1.1736231460243.789146887523561254',
    '_gcl_au': '1.1.1719554786.1736231460',
    'ak_bmsc': '50BECC795BA65F3B57F00A9E545ABFDC~000000000000000000000000000000~YAAQFFM2F3nhxKqTAQAAJZ91Pxp9wYbpmLh/uYy1Vhl4cctpfW/58yqH7D1VCSb2awyjL6UbxEv66HkuV3PKaSnLJU0anlNL7HOh+IN0VweDl4GdIYxR5KpwbZ7VSQhHS+wsK4k0UvXV4DiTkCv1ck+MdFi3K7ixjWStUZ24aCAt40Pn+S5b7WzuPmbF/J5l8NVoO2tTKHXwGXFDZdEPIUhaR9szEGGAMvINRem9qRteG5CuKG2UBN0cISTtdlcKkdsOAFQ0Qf5GyIe0N1bSjcOfo3X6KpKXAu/2wRz1C+9UTKYomOk99tfmXEOYtDdqTl2oEjb4MvYJnOewD2t0WRwNGJHSs3p9WKGEbnns0r4azUUSlp7XHvBLoNwktSXeyuvLHF6a0/mZcU5Wt3a34zlKzZVND3nhokju/FJP/HaaRXSDtOuKc6Ds125lwrRaFxuyuRerbfhh30ftUjrS3A==',
    'bm_sv': 'D56D0CCE3B6E436AB25285E9C0E73C1F~YAAQFFM2F3zkxKqTAQAA/DN2PxrUVCYX1SSQo4sY/tO5MizAorzYTTqGs/ruQ54U45q1sdSX0RwgdWAudVRJ+99unbm9AbVXmy/OFtc2zVF8jSZfVzOy7C/u0KmM1y8naMdq6afc2sOD1yjAq850d/wpZduxpx1ixYg/bTV5sk4OCf5I7ni8ur2WL/g0/X+7nSiEC9rzl5aOowWhjLJoqspYl28r9rdUDI+4a9nqCU4nrVbUhhg02Jh7qcxY9mUJ2xUfhGw=~1',
    's_pers': '%20s_vnum%3D1738348200474%2526vn%253D1%7C1738348200474%3B%20s_lv%3D1736233600089%7C1830841600089%3B%20s_lv_s%3DFirst%2520Visit%7C1736235400089%3B%20gpv_pn%3Dfunnel%253Adomestic%2520cabs%253Alisting%7C1736235400092%3B%20s_invisit%3Dtrue%7C1736235400093%3B%20s_nr3650%3D1736233600095-New%7C2051593600095%3B%20s_nr30%3D1736233600095-New%7C1738825600095%3B%20s_nr120%3D1736233600096-New%7C1746601600096%3B%20s_nr7%3D1736233600097-New%7C1736838400097%3B',
    's_sess': '%20s_cc%3Dtrue%3B%20s_sq%3D%3B%20tp%3D2492%3B%20s_ppv%3Dfunnel%25253Adomestic%252520cabs%25253Alisting%252C47%252C47%252C1159%3B',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,tr;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': 'dvid=c39e6874-ae2a-468b-ad1a-bdd5a41c067d; bm_sz=89AC0EAD62B5D7509EA75552834CEA99~YAAQFFM2F1PhxKqTAQAAgpl1PxpepyhB1PV0G7xU6qmcWn4JHAoXiP+vfcllvrMdL6mF9XJUkjWdBIp3JygyOb1dIOXAbywbrOLb3xb75KHrb9O4IriorheShmrGuUi/DeDaH90zyhwUFphBJ4mlxbjZrCrd9CPr7DvaD4A8/W/82GlKiS8872UnWwlh6CsJJQpO0DwcfzSiiAxkMOVimnPBb8ounIFYNhAolbP0GxK37YkO2PrCDXh4Kd0yAlDwnjCAZwLuFNAUdmawnBKNxaj5gX0YK6hJ44R6PJGaHGE4Yya10v3ddCdZCmh5kO0CXy6CnAUum8hOT5TR5X8MgzHJjnJfSg5bSktzx3xRgFX4ZBQWavZ4jdzbDenZwpk053sUeFaF+ClBKfGKUGFGA9le~3159605~4408376; AMCVS_1E0D22CE527845790A490D4D%40AdobeOrg=1; s_ecid=MCMID%7C35180419887856374372291499899633882820; _abck=E122D893CEEA624513D06C55CC081557~0~YAAQFFM2F1/hxKqTAQAAV5x1Pw317zUOdL5TEys7vXPsWGg7PuuOAPclwR7cX2auN5Jce2LCebXRUOtkB+X/sn7IYF4IVoY8ip2xl+wlDRw/QhRoivT4yZbVNQ46fjSFJwZHbF0f3+ZMgD0gVJrs0utT0tcudD04u3uTR26f+BU3HRvxMwdmsSEo2sBaDisqxABNGd543LSOFib9fmw6JWUMhzS1ppfpXDWRbfYJkY9PjV6nz/v/x2zIef54RB0lLhIP9qO/4drf4lK8uEq+wgxocm0b3vsDkFS6i5pjNiOyqS5g81TXT1Dqx4A+amQtixnpsCvTymKeySkk0dUfUHiJ8I40s7qN7t2tGEvSPH6PFAIG8g4ICcNRnTNDsPXKBOUKI4YbmwbEITs5hw4eF8RlsqX6qt3rux1aSY9W6noMlisOMqq1kv7785zbidIg1v4Gguk+CVglccew0p0aaa4xGFrUPDkfbqqPxIGJ0G4UZ3TT~-1~||0||~-1; AMCV_1E0D22CE527845790A490D4D%40AdobeOrg=1099438348%7CMCIDTS%7C20096%7CMCMID%7C35180419887856374372291499899633882820%7CMCAAMLH-1736836259%7C12%7CMCAAMB-1736836259%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1736238659s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.1.0; _fbp=fb.1.1736231460243.789146887523561254; _gcl_au=1.1.1719554786.1736231460; ak_bmsc=50BECC795BA65F3B57F00A9E545ABFDC~000000000000000000000000000000~YAAQFFM2F3nhxKqTAQAAJZ91Pxp9wYbpmLh/uYy1Vhl4cctpfW/58yqH7D1VCSb2awyjL6UbxEv66HkuV3PKaSnLJU0anlNL7HOh+IN0VweDl4GdIYxR5KpwbZ7VSQhHS+wsK4k0UvXV4DiTkCv1ck+MdFi3K7ixjWStUZ24aCAt40Pn+S5b7WzuPmbF/J5l8NVoO2tTKHXwGXFDZdEPIUhaR9szEGGAMvINRem9qRteG5CuKG2UBN0cISTtdlcKkdsOAFQ0Qf5GyIe0N1bSjcOfo3X6KpKXAu/2wRz1C+9UTKYomOk99tfmXEOYtDdqTl2oEjb4MvYJnOewD2t0WRwNGJHSs3p9WKGEbnns0r4azUUSlp7XHvBLoNwktSXeyuvLHF6a0/mZcU5Wt3a34zlKzZVND3nhokju/FJP/HaaRXSDtOuKc6Ds125lwrRaFxuyuRerbfhh30ftUjrS3A==; bm_sv=D56D0CCE3B6E436AB25285E9C0E73C1F~YAAQFFM2F3zkxKqTAQAA/DN2PxrUVCYX1SSQo4sY/tO5MizAorzYTTqGs/ruQ54U45q1sdSX0RwgdWAudVRJ+99unbm9AbVXmy/OFtc2zVF8jSZfVzOy7C/u0KmM1y8naMdq6afc2sOD1yjAq850d/wpZduxpx1ixYg/bTV5sk4OCf5I7ni8ur2WL/g0/X+7nSiEC9rzl5aOowWhjLJoqspYl28r9rdUDI+4a9nqCU4nrVbUhhg02Jh7qcxY9mUJ2xUfhGw=~1; s_pers=%20s_vnum%3D1738348200474%2526vn%253D1%7C1738348200474%3B%20s_lv%3D1736233600089%7C1830841600089%3B%20s_lv_s%3DFirst%2520Visit%7C1736235400089%3B%20gpv_pn%3Dfunnel%253Adomestic%2520cabs%253Alisting%7C1736235400092%3B%20s_invisit%3Dtrue%7C1736235400093%3B%20s_nr3650%3D1736233600095-New%7C2051593600095%3B%20s_nr30%3D1736233600095-New%7C1738825600095%3B%20s_nr120%3D1736233600096-New%7C1746601600096%3B%20s_nr7%3D1736233600097-New%7C1736838400097%3B; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3D%3B%20tp%3D2492%3B%20s_ppv%3Dfunnel%25253Adomestic%252520cabs%25253Alisting%252C47%252C47%252C1159%3B',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

params = {
    'fromCity': '{"airport":true,"address":"Ahmedabad International Airport, airport, Ahmedabad, Gujarat, India","latitude":23.0716999,"longitude":72.61995999999999,"pincode":"382405","place_id":"ChIJ384AuyiBXjkR656MJ9Yuk5U","is_city":false,"city":"Ahmedabad","city_code":null,"google_city":"Ahmedabad","state":"Gujarat","is_airport":true,"main_text":null,"mainText":null,"secondary_text":null,"country":"India","country_code":"IN"}',
    'toCity': '{"airport":true,"address":"Surat Airport","latitude":21.114061,"longitude":72.741792,"pincode":null,"place_id":"GhIJwr8IGjMdNUARzhsnhXkvUkA","is_city":false,"city":"Surat","city_code":null,"google_city":"Surat","state":"Gujarat","is_airport":true,"main_text":null,"mainText":null,"secondary_text":null,"country":"India","country_code":"IN"}',
    'tripType': 'OW',
    'departDate': '09-01-2025',
    'pickupTime': '10:00',
    'returnDate': '',
    'dropTime': '',
    'packageKey': '',
    'fromAirport': 'true',
    'toAirport': 'true',
    'sourceAirportId': '0',
    'destinationAirportId': '0',
    'stopOvers': '[]',
    'intlFlow': 'false',
}


for atampt in range(1, 50):
    response = requests.get(
        'https://cabs.makemytrip.com/dt_cabsListing?fromCity=%7B%22airport%22%3Atrue%2C%22address%22%3A%22Ahmedabad%20International%20Airport%2C%20airport%2C%20Ahmedabad%2C%20Gujarat%2C%20India%22%2C%22latitude%22%3A23.0716999%2C%22longitude%22%3A72.61995999999999%2C%22pincode%22%3A%22382405%22%2C%22place_id%22%3A%22ChIJ384AuyiBXjkR656MJ9Yuk5U%22%2C%22is_city%22%3Afalse%2C%22city%22%3A%22Ahmedabad%22%2C%22city_code%22%3Anull%2C%22google_city%22%3A%22Ahmedabad%22%2C%22state%22%3A%22Gujarat%22%2C%22is_airport%22%3Atrue%2C%22main_text%22%3Anull%2C%22mainText%22%3Anull%2C%22secondary_text%22%3Anull%2C%22country%22%3A%22India%22%2C%22country_code%22%3A%22IN%22%7D&toCity=%7B%22airport%22%3Atrue%2C%22address%22%3A%22Surat%20Airport%22%2C%22latitude%22%3A21.114061%2C%22longitude%22%3A72.741792%2C%22pincode%22%3Anull%2C%22place_id%22%3A%22GhIJwr8IGjMdNUARzhsnhXkvUkA%22%2C%22is_city%22%3Afalse%2C%22city%22%3A%22Surat%22%2C%22city_code%22%3Anull%2C%22google_city%22%3A%22Surat%22%2C%22state%22%3A%22Gujarat%22%2C%22is_airport%22%3Atrue%2C%22main_text%22%3Anull%2C%22mainText%22%3Anull%2C%22secondary_text%22%3Anull%2C%22country%22%3A%22India%22%2C%22country_code%22%3A%22IN%22%7D&tripType=OW&departDate=09-01-2025&pickupTime=10%3A00&returnDate=&dropTime=&packageKey=&fromAirport=true&toAirport=true&sourceAirportId=0&destinationAirportId=0&stopOvers=%5B%5D&intlFlow=false',
        # params=params,
        # cookies=cookies,
        headers=headers
    )
    print(response.text)
    print(atampt, response.status_code)