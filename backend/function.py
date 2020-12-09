import pymongo
from pymongo import MongoClient
from bson import json_util
import json

client = MongoClient('mongodb://localhost:27017/')

database = client['TMDT']
collection = database['product']

class Users:
    def List_user(self):
        list_users = []
        posts = collection.find()
        for post in posts:
            list_users.append(post)
        return json.loads(json_util.dumps(list_users))
    #Lay top san pham ban chay
    def List_top(self):
        query = {}
        projection = {}
        projection["image"] = 1.0
        projection["num_purchase"] = 1.0
        projection["name"] = 1.0
        projection["_id"] = 0.0

        sort = [ (u"num_purchase", -1) ]

        cursor = collection.find(query, projection = projection, sort = sort, limit = 10)
        try:
            for doc in cursor:
                print(doc)
        finally:
            client.close()

    #Hien detail san pham
    def detail(self,ten_sp):
        myquery = { "name": ten_sp },{"description":1,"_id":0}
        cursor = collection.find(myquery)
        try:
            for doc in cursor:
                print(doc)
        finally:
            client.close()

    #Searching sp theo ten
    def Search_name(self,ten_sp):
        myquery = { "ten_sp": { "$regex": ten_sp } }

        mydoc = collection.find(myquery)

        for x in mydoc:
            print(x)

    #Filter money
    def Filter_Money(self,gt1,gt2):
        cursor = collection.find({$and:[{price_list:{$gt:gt1}},{price_list:{$lt:gt2}}]})
        for doc in cursor:
            print(doc)

    #Filter category
    def Filter_Category(self,tmp):

    #Register
    def Register(self,user,passwd,name,email,avatar):    
        client = MongoClient("mongodb://host:port/")
        database = client["tmdt"]
        collection = database["user"]
        mydict = { "user": user, "pwd": passwd,"name" : name, "email" : email, "avatar" : avatar }
        x = collection.insert_one(mydict)

        

# print(collection.find())
print(Users().List_top())

