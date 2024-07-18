import csv
import json
from pymongo import MongoClient,ASCENDING,DESCENDING, errors
from datetime import datetime
from extension_urls import DB_CONNECTION_URLS, INDEX_TUPLES



# Function to connect to MongoDB
def connect_to_mongodb(ext_name, db_name, collection):
    MONGO_URI = DB_CONNECTION_URLS[db_name][ext_name]
    s = MONGO_URI
    DATABASE_NAME = s[s.rindex('/')+1 :  s.index('?')]
    print("Extracted db name", DATABASE_NAME)
    # DATABASE_NAME = f"{ext_name}_{db_name}"  
    COLLECTION_NAME = collection
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    print("Connected to ", db, collection)
    return client, db, collection

# Function to read data from Excel/CSV
def read_data(file_path):
    if file_path.endswith(".xlsx"):
        import pandas as pd
        data = pd.read_excel(file_path).to_dict(orient="records")
    elif file_path.endswith(".csv"):
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
    else:
        raise ValueError("Unsupported file format")
    return data

# Function to modify object
def modify_object(data_object, active):
    # Modify data_object based on your needs
    status = "ACTIVE" if active else "INACTIVE"
    modified_object = {
        "store_name" : data_object["store_name"],
        "store_id": int(data_object["store_id"]), 
        "store_code": data_object["fynd_store_code"],
        "company_id": int(data_object["company_id"]),
        "store_type": "high_street",
        "status": status,
        "created_on": datetime.now(),
        "modified_on": datetime.now(),
        "modified_by": "utkarshjain_gofynd_com_77178",
        "created_by": "utkarshjain_gofynd_com_77178"
    } 

    return modified_object

# Function to insert data into MongoDB for all records 
def insert_data(collection, data, active=False):
    count =0
    for record in data:
        modified_record = modify_object(record, active)
        print("\n",modified_record,"\n\n")
        collection.update_one({'store_id': modified_record["store_id"]}, {'$set': modified_record}, upsert=True)
        count +=1
        # collection.insert_one(modified_record)
    print(f"{count} Data inserted successfully!")

# Main function
def add_store_data(ext_name, file_name, active):
    print("adding store data >>>>>>>>>>>>>>>>>>>")
    # Replace with your file path
    file_path = f"/Users/utkarshjain/Projects/shatter/migration/store_ids/{file_name}.csv"

    # Read data
    data = read_data(file_path)
    print(data)
    # Connect to MongoDB
    client, db, collection = connect_to_mongodb(ext_name)
    print(client, db, collection)
    # # Insert data
    insert_data(collection, data, active)

    # Close connection
    client.close()


def add_index(ext_name, db_name, collection, index_cols):
    print("Adding index for", db_name, ext_name)
    client, db, collection = connect_to_mongodb(ext_name, db_name, collection)
    try:
        print("creating index ...")
        collection.create_index(index_cols)  
        print("Index created successfully!")
    except errors.OperationFailure as e:
        print("Error creating index:", e)

    # Close the connection
    client.close()

# add_store_data("eshop", "eshopbox", True)


 # * call this function for adding index in the required dbs 
# index_cols = [("store_id", ASCENDING), ("store_name", DESCENDING)]
# add_index(
#     ext_name="rblfurniture",
#     db_name="ext",
#     collection="store",
#     index_cols=index_cols
# )
    

for ext_name in DB_CONNECTION_URLS["logs"]:
    collection_name = "shipment_event_log"
    index_cols = INDEX_TUPLES[collection_name]

    for ind_col in index_cols:
        print("indexed columns >>>> ",ind_col)
        add_index(
            ext_name=ext_name,
            db_name="logs",
            collection=collection_name,
            index_cols=ind_col
        )
        print("--------------------------------------------------------------")
        


"""
    ext_name = name of extension on pod
    db_name = ext_name + _ext
    file_name = ext_name 
    active = True - if you want to change status to ACTIVE 

    ext_name_db_name
"""


"""
index_cols - list of tuples 
[("field1", ASCENDING), ("field2", DESCENDING)]
"""