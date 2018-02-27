from flask import Flask
from flask import request, jsonify
app = Flask(__name__)

users_infos = []
id = 0
info_list={}
@app.route('/')
def hello():
    return "Hello!!",200

@app.route('/users',methods=['POST'])
def new_user():
     global id
     id = id+1
     users_info = {
                'id':id,
                'name':request.form['name']
                }
     users_infos.append(users_info)
     return jsonify({'User Information' : users_infos}),201

@app.route('/users/<id>',methods=['GET'])
def out(id):
    for i in range(len(users_infos)):
        if int(users_infos[i]['id']) == int(id):
            return jsonify({'User Information':users_infos[i]}),200
     
@app.route('/users/<id>',methods=['DELETE'])
def delete_id(id):
    k=0
    for i in range(len(users_infos)):
        if int(users_infos[i]['id']) == int(id):
            k=i
    users_infos.pop(k)
    return jsonify({'User Information': users_infos}),204