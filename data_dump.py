import pymongo
import pandas as pd
import json
import urllib.parse
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://ayush:admin@cluster0.upyxbqo.mongodb.net/?retryWrites=true&w=majority")




DATA_FILE_PATH = "D:/Income_Predection/adult.csv"
DATABASE_NAME = "aip"
COLLECTION_NAME = "income"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows,columns:{df.shape}")

    #Convert dataframe to json format
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)