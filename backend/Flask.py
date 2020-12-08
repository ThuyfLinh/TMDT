import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
# import importlib

from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import function
app = Flask(__name__)
api = Api(app)
CORS(app)

# import pymongo
# from pymongo import MongoClient

@app.route('/get', methods=['GET'])
def get():
    project = function.Users()
    result = project.List_user()
    return{
        "statusCode": 200,
        "body": result
    }

# @app.route('/', methods=['GET'])
# def query_records():
#     name = request.args.get('name')
#     user = User.objects(name=name).first()
#     # user = User.find()
#     if not user:
#         return jsonify({'error': 'data not found'})
#     else:
#         return jsonify(user.to_json())

# @app.route('/', methods=['PUT'])
# def create_record():
#     # record = json.loads(request.data)  
#     name = request.headers.get("name")
#     email = request.headers.get("email")
#     # record = json.loads(request.data)
#     user = User(name=name,
#                 email=email)
#     user.save()
#     return jsonify(user.to_json())
#     # return record['name']
#     # return name

# @app.route('/', methods=['POST'])
# def update_record():
#     record = json.loads(request.data)
#     user = User.objects(name=record['name']).first()
#     if not user:
#         return jsonify({'error': 'data not found'})
#     else:
#         user.update(email=record['email'])
#     return jsonify(user.to_json())

# @app.route('/', methods=['DELETE'])
# def delete_record():
#     record = json.loads(request.data)
#     user = User.objects(name=record['name']).first()
#     if not user:
#         return jsonify({'error': 'data not found'})
#     else:
#         user.delete()
    # return jsonify(user.to_json())

if __name__ == "__main__":
    app.run(debug=True)