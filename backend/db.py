# from flask import Flask, request, jsonify
# from flask_mongoengine import MongoEngine
from mongoengine import *
import os
# from flask_pymongo import PyMongo
# import Users

connect("mongo-dev-db")

class User(Document):
    name = StringField()
    email = EmailField()
    def to_json(self):
        user_dict = {
            "name": self.name,
            "email": self.email
        }
        return json.dumps(user_dict)

user = User(
    name="Linh",
    email="linh@gmail.com"
).save()

print("Done")


# app = Flask(__name__)

# app.config['MONGODB_SETTINGS'] = {
#     'db': 'your_database',
#     'host': 'localhost',
#     'port': 27017
# }

# if __name__ == "__main__":
#     app.run(debug=True)