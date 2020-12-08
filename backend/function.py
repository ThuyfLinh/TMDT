import pymongo
from pymongo import MongoClient
from bson import json_util
import json

# client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

db = client['user']
collection = db['user']

class Users:
    def List_user(self):
        list_users = []
        posts = collection.find()
        for post in posts:
            list_users.append(post)
        return json.loads(json_util.dumps(list_users))

    

# print(collection.find())
print(Users().List_user())

