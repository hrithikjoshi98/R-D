import pymongo
import pandas as pd
import uuid

if __name__ == '__main__':
    MONGO_URI = "mongodb://localhost:27017/"  # Replace with your MongoDB URI
    DB_NAME = "shein_us_test"  # Replace with your database name
    COLLECTION_NAME = "shein_us"  # Replace with your collection name

    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    # Define the query to fetch only documents with status = "pending"
    query = {"status": "Pending"}

    # df = pd.read_csv('shein_us_2025_01_03.csv')
    df = pd.read_csv('shein_us_2025_01_03.csv')
    urls = df['url']
    for url in urls:
        item = {}
        item['link'] = url
        item['pdp_status'] = 'pending'
        item['review_status'] = 'pending'
        try:
            if "userID" not in item or item["userID"] is None:
                item["userID"] = str(uuid.uuid4())
            collection.insert_one(item)
            print(" = =Inserted = =")
        except Exception as e:
            print(e)