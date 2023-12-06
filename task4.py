"""
Module for working with MongoDB and managing the 'log_events' collection.

Connects to the local MongoDB server and creates the 'log_events' collection.
If the 'createdAt_1' index is not present in the collection, it creates a TTL (Time-To-Live) index
that deletes documents after 5 seconds from the 'createdAt' field.
"""

import time
from datetime import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['task']
collection = db['log_events']
indexes_info = collection.index_information()
if 'createdAt_1' not in indexes_info.keys():
    collection.create_index("createdAt", expireAfterSeconds=5)

if __name__ == '__main__':
    current_time_utc = datetime.utcnow()
    doc = {"message": "Some log message",
           "createdAt": current_time_utc}
    collection.insert_one(doc)
    time.sleep(20)

    result = collection.find_one({"message": "Some log message"})
    if result:
        print("Документ найден:", result)
    else:
        print("Документ был успешно удален.")
