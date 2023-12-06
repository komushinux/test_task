import time
from datetime import datetime

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['task']

collection = db['log_events']

if __name__ == '__main__':
    current_time_utc = datetime.utcnow()
    doc = {
        "message": "Some log message",
        "createdAt": current_time_utc
    }

    collection.insert_one(doc)

    time.sleep(10)

    indexes_info = collection.index_information()
    print(indexes_info)

    result = collection.find_one({"message": "Some log message"})
    if result:
        print("Документ найден:", result)
    else:
        print("Документ был успешно удален.")
