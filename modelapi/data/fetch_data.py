from pymongo import MongoClient
import certifi
import pandas as pd
import os
# from dotenv import load_dotenv

# load_dotenv()
uri = os.getenv("MONGO_URL_ID")
db_name = os.getenv("DB_NAME_ID")
collection_name = os.getenv("COLLECTION_NAME_ID")

client = MongoClient(uri, tlsCAFile=certifi.where())
db = client[db_name]
collection = db[collection_name]

def fetchData():
    data = list(collection.find())
    df = pd.DataFrame(data)
    df.drop(columns = ['_id'], inplace = True)

    # client.close()
    # print(df.head())
    return df
