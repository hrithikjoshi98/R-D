import json
import random
from itertools import product
import pymongo
import requests
from datetime import datetime
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.parse
from colorama import Fore


#todo - Page save function
def get_save_dir(region, pagetype, domain):
    """
    Constructs a save directory based on root path, region, domain, and current date.
    """
    # Define the common root path
    root_path = r"D:\Krushil_Gajjar\HTMLs"
    current_date = datetime.now().strftime("%Y_%m_%d")
    save_dir = os.path.join(root_path, region, domain, pagetype, current_date)
    os.makedirs(save_dir, exist_ok=True)
    return save_dir

# Example Usage
region = "UK"  # Replace this dynamically as per your use case
domain = "Shein"  # Replace this dynamically as per your use case
pagetype = "review"  # Replace this dynamically as per your use case
# Get the save directory
SAVE_DIR = get_save_dir(region, pagetype, domain)
print(f"Saving files to: {SAVE_DIR}")

token = "aa48e53ef4934d95a56acecacaec8fe454ebf634a98"

# Global counters
success_count = 0
failed_count = 0
exception_count = 0

def make_request(document):
    """
    Function to make a single request and handle success or failure.
    """
    global success_count, failed_count, exception_count

    # Todo - Netnut Proxy Declaration
    random_number = random.randint(10000000, 99999999)
    username = f'actowiz-res-US-any-sid-{random_number}'
    password = 'yYNSa0hbTdfNUIh'
    server = 'gw.ntnt.io'
    port = '5959'
    proxy = {
        'http': f'http://{username}:{password}@{server}:{port}',
        'https': f'http://{username}:{password}@{server}:{port}'
    }

    url = document['link']  # Assuming the document has a field 'url'
    doc_id = document['_id']  # MongoDB document ID

    try:
        url = str(url).strip()
        url = url.split('html?')[0]
        url = str(url) + "html"
    except:
        url = url

    try:
        pid = str(url.split("-")[-1]).replace(".html",'')
    except Exception as e:
        print(f"{Fore.RED}Blank PID is generated.....")
        pid = ''

    # todo - review url
    try:
        # Encode the query URL
        target_url = f'https://www.shein.co.uk/bff-api/product/get_goods_detail_realtime_data?_ver=1.1.8&_lang=en&goods_id={pid}&mallCode=1&isUserSelectedMallCode=1'
        encoded_query_url = urllib.parse.quote(target_url, safe='')

        # todo - sending req using proxy (Scrape Do)
        url = f'''http://api.scrape.do?token={token}&url={encoded_query_url}&super=true'''
        response = requests.request("GET", url)

        page_resp = response.text

        if ('comment' in page_resp) and ("comment_rank_average" in response.text) and ("product_comments" in response.text):
            success_count += 1
            print(f"Success Response {response.status_code} ------> {pid}")
            FilePath = SAVE_DIR + f'\\Success_{pid}.html'
        else:
            failed_count += 1
            print(f"Failed Response {response.status_code} ------> {pid}")
            FilePath = SAVE_DIR + f'\\Fail_{pid}.html'

        # todo - saving html pages and inserting data on every page at scrolling time
        page_resp = response.text
        with open(FilePath, 'w', encoding='utf-8') as f:
            f.write(page_resp)

        json_data = json.loads(page_resp)
        rating = json_data.get('info').get('comment').get('comments_overview').get('localSiteScore')

        product_comments = json_data.get('info').get('comment').get('product_comments')
        comments_ls = []
        for comment in product_comments:
            p_comment = comment.get('content')
            add_time = comment.get('add_time')
            comment_time = comment.get('comment_time')
            comment_id = comment.get('comment_id')
            comment_by = comment.get('user_name')
            goods_id = comment.get('goods_id')  # Fix the key to extract goods_id correctly

            # Only add the comment if it exists
            if p_comment:
                comments_ls.append({
                    "content": p_comment,
                    "add_time": add_time,
                    "comment_time": comment_time,
                    "comment_id": comment_id,
                    "comment_by": comment_by,
                    "goods_id": goods_id
                })

        # Prepare the update dictionary
        update_dict = {
            "review_status": "Done",
            "rating": rating,
            "comments": comments_ls,  # Store the list of comment dictionaries
            "review_status_code": response.status_code
        }
        # Update the MongoDB document with the result
        collection.update_one(
            {"_id": doc_id},
            {"$set": update_dict}
        )

    except Exception as e:
        exception_count += 1
        print(f"Failed Response Exception --> {e} ------> {pid}")

# MongoDB connection setup
MONGO_URI = "mongodb://localhost:27017/"  # Replace with your MongoDB URI
DB_NAME = "shein_test"  # Replace with your database name
COLLECTION_NAME = "shein_uk"  # Replace with your collection name

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

MAX_WORKERS = 8  # Number of threads to use

documents = collection.find({"review_status": "pending"}).limit(100)

# ThreadPoolExecutor implementation
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = [executor.submit(make_request, doc) for doc in documents]

    for future in as_completed(futures):
        # Optional: Handle each task result as it completes
        pass

# Summary
print(f"\nSummary:")
print(f"Total Success: {success_count}")
print(f"Total Failed: {failed_count}")
print(f"Total Exceptions: {exception_count}")