import json
import random
from typing import Iterable, Union
import pandas as pd
import scrapy
from scrapy import Request, Spider
from scrapy.cmdline import execute
import os
from twisted.internet.defer import Deferred
from datetime import datetime

def df_cleaning(df):
    # Drop Unnamed columns
    df = df.loc[:, ~df.columns.str.contains('Unnamed')]
    # Replace empty strings with 'N/A'
    df = df.replace('', 'N/A').replace('None', 'N/A')
    df.fillna('N/A', inplace=True)
    # Add id column
    df.insert(0, 'id', range(1, len(df) + 1))
    # Convert column headers to lowercase and replace spaces with underscores
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

def date_convert(date_in_miliseconds: int):
    timestamp = date_in_miliseconds / 1000  # Convert milliseconds to seconds
    dt_object = datetime.utcfromtimestamp(timestamp)
    # Format the datetime to 'dd/mm/yyyy'
    formatted_date = dt_object.strftime('%d/%m/%Y')
    return formatted_date

def prioritize_columns(df, priority_columns):
    df = df[priority_columns + [col for col in df.columns if col not in priority_columns]]
    return df

class CabsSpider(scrapy.Spider):
    name = "cabs"
    browsers = [
        'chrome99',
        'chrome100',
        'chrome101',
        'chrome104',
        'chrome107',
        'chrome110',
        'edge99',
        'edge101',
        'safari15_5'
    ]

    body1 = '{"preApplyCouponCode":null,"departure_date":"09-01-2025","return_date":null,"trip_type":"AT","pickup_time":"10:00","drop_time":null,"source_location":{"airport":true,"address":"Ahmedabad International Airport, airport, Ahmedabad, Gujarat, India","latitude":23.0716999,"longitude":72.61995999999999,"pincode":"382405","place_id":"ChIJ384AuyiBXjkR656MJ9Yuk5U","is_city":false,"city":"Ahmedabad","city_code":null,"google_city":"Ahmedabad","state":"Gujarat","is_airport":true,"main_text":null,"mainText":null,"secondary_text":null,"country":"India","country_code":"IN"},"destination_location":{"city":"Surat","stn":"Surat Airport","id":"GhIJwr8IGjMdNUARzhsnhXkvUkA","is_airport":true,"is_city":false,"address":"Surat Airport","latitude":21.114061,"longitude":72.741792,"pincode":null,"place_id":"GhIJwr8IGjMdNUARzhsnhXkvUkA","google_city":"Surat","state":"Gujarat","country":"India","country_code":"IN"},"source_city":null,"destination_city":null,"booking_device":"desktop","package_key":null,"fetch_package_list":false,"airport_cabs_enabled":true,"hr_cabs_enabled":true,"book_mode":"D","at_cross_sell_request":false,"profile_type":"PERSONAL","session_token":"","email":"","is_e_pass_enabled":true,"is_custom_payment_allowed":true,"is_default_search":true,"connector_search":false,"show_kit_enabled_cabs":true,"is_intercity_2":true,"rating_show":true,"mybiz_traveller_email":null,"mybiz_traveller_type":null,"is_other_cabs_enabled":true,"pokus_flags":[{"key":"OS_Listing_Packages","flag":true},{"key":"Listing_Part_Payment","flag":false},{"key":"Listing_Assisted_Widget_web","flag":false},{"key":"review_assisted_widget_dweb","flag":true},{"key":"Mybiz_Assured_Cab_dweb","flag":true}],"fetch_ryd_cabs":true,"funnel_source":null,"ih_flow":false,"stopovers":[]}'
    body2 = '{"preApplyCouponCode":null,"departure_date":"08-01-2025","return_date":null,"trip_type":"AT","pickup_time":"10:00","drop_time":null,"source_location":{"city":"Ahmedabad","stn":"Gujarat, India","id":"ChIJSdRbuoqEXjkRFmVPYRHdzk8","is_airport":false,"is_city":true,"address":"Ahmedabad, Gujarat, India","latitude":23.022505,"longitude":72.5713621,"pincode":null,"place_id":"ChIJSdRbuoqEXjkRFmVPYRHdzk8","google_city":"Ahmedabad","state":"Gujarat","country":"India","country_code":"IN"},"destination_location":{"city":"Ahmedabad","stn":"","id":"ChIJ384AuyiBXjkR656MJ9Yuk5U","is_airport":true,"is_city":false,"address":"Ahmedabad International Airport, airport, Ahmedabad, Gujarat, India","latitude":23.0716999,"longitude":72.61995999999999,"pincode":"382405","place_id":"ChIJ384AuyiBXjkR656MJ9Yuk5U","google_city":"Ahmedabad","state":"Gujarat","country":"India","country_code":"IN"},"source_city":null,"destination_city":null,"booking_device":"desktop","package_key":null,"fetch_package_list":false,"airport_cabs_enabled":true,"hr_cabs_enabled":true,"book_mode":"D","at_cross_sell_request":false,"profile_type":"PERSONAL","session_token":"","email":"","is_e_pass_enabled":true,"is_custom_payment_allowed":true,"is_default_search":true,"connector_search":false,"show_kit_enabled_cabs":true,"is_intercity_2":true,"rating_show":true,"mybiz_traveller_email":null,"mybiz_traveller_type":null,"is_other_cabs_enabled":true,"pokus_flags":[{"key":"OS_Listing_Packages","flag":true},{"key":"Listing_Part_Payment","flag":false},{"key":"Listing_Assisted_Widget_web","flag":false},{"key":"review_assisted_widget_dweb","flag":true},{"key":"Mybiz_Assured_Cab_dweb","flag":true}],"fetch_ryd_cabs":true,"funnel_source":null,"ih_flow":false,"stopovers":[]}'
    body_list = [body1, body2]
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

    main_list = []

    def start_requests(self):
        os.makedirs('C:/hrithik/Research and Analysis Wing/cabs_makemytrip_com/scrapy/cabs_makemytrip/cabs_makemytrip/files', exist_ok=True)
        for pos, attempt in enumerate(self.body_list):
            url = 'https://cabs.makemytrip.com/desktop/searchV2'
            selected_browser = random.choice(self.browsers)
            yield scrapy.Request(
                url,
                method='POST',
                dont_filter=True,
                headers=self.headers,
                body=attempt,
                meta={"impersonate": selected_browser, 'attempt': attempt, 'pos': pos},  # USED SCRAPY IMPERSONATE TO PREVENT 403 ERROR
                callback=self.parse)


    def parse(self, response, **kwargs):
        attempt = response.meta['attempt']
        pos = response.meta['pos']
        try:
            json_d = json.loads(response.text)
            print(response.text)
            # print(response.status, 'fohurfjdsfiq', attempt)
            if response.status == 200:
                with open('C:/hrithik/Research and Analysis Wing/cabs_makemytrip_com/scrapy/cabs_makemytrip/cabs_makemytrip/files' + f'/makemytrip_{str(pos)}.html', 'w', encoding='UTF-8') as file:
                    file.write(response.text)
            cab_list = json_d['response']['cab_list']
            for i in cab_list:
                dic = {}
                jd = json.loads(attempt)
                dic['source'] = jd['source_location']['address']
                dic['destination'] = jd['destination_location']['address']
                # price = i['fare_details']['display_properties'][0]['Base Fare']
                dic['type'] = i['type']
                dic['package'] = i['package']
                dic['vehicle_model_type'] = i['vehicle_model_type']
                dic['vendor_id'] = i['vendor_id']
                dic['supplier_id'] = i['supplier_id']
                dic['supplier_name'] = i['supplier_name']
                print(i['supplier_name'])
                dic['vendor_name'] = i['vendor_name']
                dic['vehicle_image'] = i['vehicle_image']
                dic['vehicle_model'] = i['vehicle_model']

                try:
                    cab_utilities = i['cab_utilities']
                    cab_utility = ' | '.join([cab_utility_txt['text'] for cab_utility_txt in cab_utilities])
                except Exception as e:
                    cab_utility = ''
                    print('cab_utilities', e)
                dic['cab_utility'] = cab_utility

                try:
                    fare_details_list = i['fare_details']['display_properties']
                    for detail in fare_details_list:
                        for key, value in detail.items():
                            dic[str(key).lower().replace(' ', '_').strip()] = value
                    # fare_details = [detail for detail in fare_details_list]
                except Exception as e:
                    print('fare_details_list', e)

                try:
                    for detail in i['fare_breakup_list']:
                        dic['fare_'+detail['displayName']] = detail['value']
                except Exception as e:
                    print('fare_breakup_list', e)

                dic['overall_trip_distance_in_kms'] = i['journey_detail']['overall_trip_distance_in_kms']
                dic['overall_trip_duration_in_minutes'] = i['journey_detail']['overall_trip_duration_in_minutes']

                dic['per_km_extra_charge'] = i['cab_fare_detail']['per_km_extra_charge']
                dic['partial_payable_amount'] = i['cab_fare_detail']['partial_payable_amount']
                dic['cancellation_penalty'] = i['cab_fare_detail']['cancellation_penalty']

                dic['coupon_code'] = i['cab_fare_detail']['coupon_code']
                dic['coupon_amount'] = i['cab_fare_detail']['coupon_amount']
                dic['driver_charge'] = i['cab_fare_detail']['driver_charge']

                try:
                    dic['overall_rating'] = i['ratings_display']['overall_rating']
                except Exception as e:
                    dic['overall_rating'] = ''

                try:
                    dic['no_of_ratings'] = i['ratings_display']['no_of_ratings']
                except Exception as e:
                    dic['no_of_ratings'] = ''

                try:
                    dic['cab_condition'] = i['ratings_display']['cab_condition']
                except Exception as e:
                    dic['cab_condition'] = ''

                try:
                    dic['driver_behavior'] = i['ratings_display']['driver_behavior']
                except Exception as e:
                    dic['driver_behavior'] = ''

                try:
                    dic['no_of_reviews'] = i['ratings_display']['no_of_reviews']
                except Exception as e:
                    dic['no_of_reviews'] = ''

                for pos, penalty in enumerate(i['cancellation_timeline']['cancellationTimeLineInfoList']):
                    dic[f'penaltyPercent_{pos}'] = penalty['penaltyPercent']
                    dic[f'validFrom_{pos}'] = date_convert(int(penalty['validFrom']))
                    dic[f'validTill_{pos}'] = date_convert(int(penalty['validTill']))
                    dic[f'penaltyText_{pos}'] = str(penalty['penaltyText']).strip()
                    dic[f'timeText_{pos}'] = str(penalty['timeText']).strip()

                dic['penaltyStartTimestamp'] = date_convert(int(i['cancellation_timeline']['penaltyStartTimestamp']))
                dic['penaltyEndTimestamp'] = date_convert(int(i['cancellation_timeline']['penaltyEndTimestamp']))
                dic['penaltyAfterFreeCancellation'] = i['cancellation_timeline']['penaltyAfterFreeCancellation']

                print(dic)
                print('\n\n')

                self.main_list.append(dic)
        except Exception as e:
            print('Error to get cabs', e)
        print('\n\n')

    def close(self, spider: Spider, reason: str):
        df = pd.DataFrame(self.main_list)
        df = df_cleaning(df)

        priority_columns = ["id"]
        df = prioritize_columns(df, priority_columns)

        input_file_path = f"C:/hrithik/Research and Analysis Wing/cabs_makemytrip_com/scrapy/cabs_makemytrip/cabs_makemytrip/files/cabs_makemytrip_{datetime.now().strftime('%Y%m%d')}.xlsx"
        df.to_excel(input_file_path, index=False)

if __name__ == '__main__':
    execute("scrapy crawl cabs".split())