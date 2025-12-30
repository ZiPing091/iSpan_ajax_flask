from flask_restful import Resource
from flask import request

class Items(Resource):
    # GET /items
    def get(self):                                                
        return {'message': '讀取所有資料'}, 200
    # POST /items
    def post(self):    
        data = request.get_json()
        return {'message': f'新增{data["name"]},{data["email"]}'}, 201

class Item(Resource):
    def get(self, id):                                           # GET /items/<id>   
        return {'message': f'根據{id}讀取資料'}, 200
    def put(self, id):     
        data = request.get_json()                                      # PUT /items/<id>    
        return {'message': f'根據{id}修改{data["name"]}'}, 200   
    def delete(self, id):                                      # DELETE /items/<id>
        return {'message': f'根據{id}刪除資料'},200
