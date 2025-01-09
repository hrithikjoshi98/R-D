import hashlib
import json
import os
import random
import pandas as pd
from curl_cffi import requests
# import requests
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


# inputs
# source_location_name = 'Surat station, Railway Station Circle, Railway Station Area, Varachha, Surat, Gujarat, India'
# destination_location_name = 'Ahmedabad Railway Station, Kalupur Railway Station Road, Sakar Bazzar, Kalupur, Ahmedabad, Gujarat, India'
# departure_date = "10-01-2025"
# pickup_time = "10:00"
main_list = []

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,tr;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://cabs.makemytrip.com',
    'referer': 'https://cabs.makemytrip.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

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

class VehicleRequest(BaseModel):
    source: str
    destination: str
    date: str
    time: str

class VehicleResponse(BaseModel):
    car_name: str
    car_type: str
    package: str
    vehicle_model_type: str
    supplier_name: str
    fare_price: str
    trip_distance: str

def df_cleaning(df):
    # Convert Columns to String
    df = df.astype(str)
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

def page_save(response, name):
    with open(
        'C:/hrithik/Research and Analysis Wing/cabs_makemytrip_com/simple_python/files' + f'/{name}.html',
        'w', encoding='UTF-8') as file:
        file.write(response.text)

def request_for_location_details(query):
    params = {
        'query': query,
        'tripType': 'OW',
        # 'tripType': 'AT',
        'requestFor': 'from',
        'isCorporate': 'false',
        'countryCode': 'IN',
    }
    response = requests.get(
        'https://cabs.makemytrip.com/autocomplete/v3',
        params=params,
        headers=headers
    )

    json_data = json.loads(response.text)
    print(json_data)
    address = json_data.get('res')[0].get('structured_formatting').get('secondary_text')  # address - description
    place_id = json_data.get('res')[0].get('place_id')  # place_id - place_id
    # city = json_data.get('res')[0].get('terms')[4].get('value')  # city, google_city
    # state = json_data.get('res')[0].get('terms')[5].get('value')  # state
    # country = json_data.get('res')[0].get('terms')[6].get('value')  # country
    # return address, place_id, city, state, country
    return address, place_id, '', '', ''

app = FastAPI()


# @app.post("/get-vehicle-details", response_model=VehicleResponse)
@app.post("/get-vehicle-details")
async def get_vehicle_details(request: VehicleRequest):
    source_location_name = request.source
    destination_location_name = request.destination
    source_location = request_for_location_details(source_location_name)
    destination_location = request_for_location_details(destination_location_name)
    departure_date = request.date
    pickup_time = request.time
    json_data = {
        "preApplyCouponCode": None,
        "departure_date": departure_date,
        "return_date": None,
        "trip_type": "AT",
        "pickup_time": pickup_time,
        "drop_time": None,
        "source_location": {
            "city": source_location[2],
            "stn": "",
            "id": source_location[1],
            "address": source_location[0],
            "place_id": source_location[1],
            "google_city": source_location[2],
            "state": source_location[3],
            "country": source_location[4],
            "country_code": "IN"
        },
        "destination_location": {
            "city": destination_location[2],
            "stn": "",
            "id": destination_location[1],
            "address": destination_location[0],
            "place_id": destination_location[1],
            "google_city": destination_location[2],
            "state": destination_location[3],
            "country": destination_location[4],
            "country_code": "IN"
        },
        "source_city": None,
        "destination_city": None,
        "booking_device": "desktop",
        "package_key": None,
        "fetch_package_list": False,
        "airport_cabs_enabled": True,
        "hr_cabs_enabled": True,
        "book_mode": "D",
        "at_cross_sell_request": False,
        "profile_type": "PERSONAL",
        "session_token": "",
        "email": "",
        "is_e_pass_enabled": True,
        "is_custom_payment_allowed": True,
        "is_default_search": True,
        "connector_search": False,
        "show_kit_enabled_cabs": True,
        "is_intercity_2": True,
        "rating_show": True,
        "mybiz_traveller_email": None,
        "mybiz_traveller_type": None,
        "is_other_cabs_enabled": True,
        "pokus_flags": [
            {
                "key": "OS_Listing_Packages",
                "flag": True
            },
            {
                "key": "Listing_Part_Payment",
                "flag": False
            },
            {
                "key": "Listing_Assisted_Widget_web",
                "flag": False
            },
            {
                "key": "review_assisted_widget_dweb",
                "flag": True
            },
            {
                "key": "Mybiz_Assured_Cab_dweb",
                "flag": True
            }
        ],
        "fetch_ryd_cabs": True,
        "funnel_source": None,
        "ih_flow": False,
        "stopovers": []
    }
    os.makedirs(
        'C:/hrithik/Research and Analysis Wing/cabs_makemytrip_com/scrapy/cabs_makemytrip/cabs_makemytrip/files',
        exist_ok=True)
    url = 'https://cabs.makemytrip.com/desktop/searchV2'
    selected_browser = random.choice(browsers)
    response = requests.post(
        url,
        headers=headers,
        json=json_data,
        impersonate=selected_browser,
    )
    data_string = f"{source_location_name}_{destination_location_name}_{departure_date}_{pickup_time}"

    # Use blake2b hash function to create a short unique key (digest_size=8 for a shorter hash)
    unique_key = hashlib.blake2b(data_string.encode(), digest_size=8).hexdigest()
    # Format the date and time
    formatted_date_time = datetime.now().strftime("%d%m%Y%H%M%S%f")
    # try:
    json_d = json.loads(response.text)
    print(response.text)
    if response.status_code == 200:
        response_ava = json_d.get('response')
        if response_ava:
            cab_list = response_ava.get('cab_list')

            for data in cab_list:
                dic, package_dic = {}, {}

                vehicle_model_type = data.get("vehicle_model_type", 'N/A')

                vehicle_model = data.get("vehicle_model", 'N/A')

                supplier_name = data.get("supplier_name", 'N/A')

                base_fare = 'N/A'
                fare_details = data.get("fare_details")
                if fare_details:
                    display_properties = fare_details.get("display_properties")
                    if display_properties:
                        for property in display_properties:
                            if "Base Fare" == property:
                                base_fare = display_properties.get(property, 'N/A')

                trip_distance = 'N/A'
                journey_detail = data.get("journey_detail")
                if journey_detail:
                    trip_distance = journey_detail.get("overall_trip_distance_in_kms", 'N/A')

                utilities = data.get("utilities", 'N/A')

                total_fare = 'N/A'
                cab_fare_detail = data.get("cab_fare_detail")
                if cab_fare_detail:
                    total_fare = cab_fare_detail.get("total_amount", 'N/A')

                fare_details = data.get("fare_details")
                if fare_details:
                    fare_details = fare_details.get("display_properties", 'N/A')
                # fare_details = data.get("fare_details", {}).get("display_properties", [{}])

                trip_duration = 'N/A'
                journey_detail = data.get("journey_detail")
                if journey_detail:
                    trip_duration = journey_detail.get("oneway_duration_in_minutes", 'N/A')
                # trip_duration = data.get("journey_detail", {}).get("oneway_duration_in_minutes", None)

                vendor_id = data.get("vendor_id", 'N/A')

                per_km_extra_charge = 'N/A'
                per_km_extra_charge = data.get("cab_fare_detail")
                if per_km_extra_charge:
                    per_km_extra_charge = per_km_extra_charge.get("per_km_extra_charge", 'N/A')

                # per_km_extra_charge = data.get("cab_fare_detail", {}).get("per_km_extra_charge", None)

                cab_utilities = []
                car_type = data.get("cab_utilities")
                if car_type:
                    for car in car_type:
                        if car:
                            txt = car.get("text", 'N/A')
                            cab_utilities.append(txt)

                # car_type = car_type[0].get("text", None) if len(car_type) > 0 else None

                facilities = data.get("facilities", 'N/A')

                fuel_type = data.get("fuel_type", 'N/A')

                car_description = data.get("cab_description", 'N/A')

                source_city = source_location_name
                destination_city = destination_location_name

                dic['vehicle_model'] = vehicle_model
                dic['vehicle_model_type'] = vehicle_model_type
                dic['supplier_name'] = supplier_name
                dic['base_fare'] = base_fare
                dic['trip_distance'] = trip_distance

                package_dic = {
                    "utilities": utilities,
                    "total_fare": total_fare,
                    "fare_details": fare_details,
                    "trip_duration": trip_duration,
                    "vendor_id": vendor_id,
                    "per_km_extra_charge": per_km_extra_charge,
                    "cab_utilities": cab_utilities,
                    "facilities": facilities,
                    "fuel_type": fuel_type,
                }
                dic['package'] = package_dic
                dic['car_description'] = car_description
                dic['source_city'] = source_city
                dic['destination_city'] = destination_city

                print('\n')
                main_list.append(dic)
        else:
            main_list.append(json_d)
            # name = unique_key + '_' + formatted_date_time
            # page_save(response, name)
    else:
        dic = {}
        main_list.append(json_d)
        # name = unique_key + '_' + formatted_date_time
        # page_save(response, name)
    return main_list

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
