import pymongo
from pymongo import MongoClient
from bson import json_util
import json

client = MongoClient('mongodb://localhost:27017/')

database = client['TMDT']
collection_product = database['product']
collection_user = database["user"]

class Users:
    def List_user(self):
        list_users = []
        posts = collection_product.find()
        for post in posts:
            list_users.append(post)
        return json.loads(json_util.dumps(list_users))

    #Lay top san pham ban chay
    def List_top(self):
        list_product = []
        query = {}
        projection = {}
        projection["image"] = 1.0
        projection["num_purchase"] = 1.0
        projection["name"] = 1.0
        projection["_id"] = 0.0

        sort = [ (u"num_purchase", -1) ]

        cursor = collection_product.find(query, projection = projection, sort = sort, limit = 10)
        try:
            for doc in cursor:
                list_product.append(doc)
        finally:
            client.close()
            return list_product

    #Hien detail san pham
    def detail(self,ten_sp):
        list_detail_product = []
        myquery = { "name": ten_sp}
        cursor = collection_product.find(myquery)
        try:
            for doc in cursor:
                list_detail_product.append(doc)
        finally:
            client.close()
            return list_detail_product

    #Searching sp theo ten
    def Search_name(self,ten_sp):
        list_product_search = []
        myquery = { "name": { "$regex": ten_sp } }

        mydoc = collection_product.find(myquery)

        for x in mydoc:
            list_product_search.append(x)

        return list_product_search

    #Filter money
    def Filter_Money(self,gt1,gt2):
        cursor = collection_product.find({"price_list.0.price" : {"$gte" : gt1, "$lte": gt2}})
        # db.product.find({"price_list":{price: 400000}})
        for doc in cursor:
            print(doc)

    #Filter category
    # def Filter_Category(self,tmp):

    #Register
    def Register(self,user,passwd,name,email,avatar):    
        mydict = { "user": user, "pwd": passwd,"name" : name, "email" : email, "avatar" : avatar }
        x = collection_user.insert_one(mydict)

        

# print(collection.find())
# print(Users().List_top())
# print(Users().Search_name('Điện thoại'))
print(Users().Filter_Money(4000000,4500000))

