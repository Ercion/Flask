from flask import Flask,jsonify,request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS



'''
Flask --> The flask object implements a WSGI application and acts as the central object. 
WSGI --> The Web Server Gateway Interface is a simple calling convention for web servers to forward requests to web applications or frameworks
jsonify -->  It turns the JSON output 
request.get_json --> converts the JSON object into Python data
PyMongo --> bridges Flask and PyMongo and provides some convenience helpers.
ObjectId -->  to create an ObjectId from a string
flask_cors --> A Flask extension for handling Cross Origin Resource Sharing (CORS). 
Cross-Origin Resource Sharing(CORS) --> is a protocol that enables scripts running on a browser client to interact with resources from a different origin. 

'''



app= Flask(__name__)

'''
I have created ercion db on my local MongoDB and I created task collection.

'''

app.config['MONGO_DBNAME'] = 'ercion'
app.config['MONGO_URI'] ='mongodb://localhost:27017/ercion'

mongo = PyMongo(app)

CORS(app)

@app.route('/')
def welcome_home():
    return jsonify(message='Welcome Home')


@app.route('/api/tasks',methods=['GET'])
def get_all_tasks():
    tasks=mongo.db.tasks

    result= []

    for field in tasks.find():
        result.append({'_id':str(field['_id']),'title':field['title']})

    return jsonify(result)


@app.route('/api/tasks',methods=['POST'])
def add_task():
    tasks = mongo.db.tasks
    title= request.get_json()['title']

    task_id=tasks.insert({'title':title})
    new_task = tasks.find_one({'_id':task_id})

    result = {'title':new_task['title']}

    return jsonify({'result':result})


'''
title= request.get_json()['title']

or 

get_title= request.get_json()

title=get_title['title']


'''


@app.route('/api/task/<id>',methods=['PUT'])
def update_task(id):
    tasks=mongo.db.tasks
    title=request.get_json()['title']

    tasks.find_one_and_update(
    {'_id':ObjectId(id)},
    {"$set":{"title":title}},upsert=False)

    new_task=tasks.find_one({'_id':ObjectId(id)})

    result = {'title':new_task['title']}

    return jsonify({'result':result})


@app.route('/api/task/<id>',methods=['DELETE'])
def delete_task(id):
    tasks=mongo.db.tasks
    
    response = tasks.delete_one({'_id':ObjectId(id)})
    
    if response.deleted_count==1:
        result = {'message':'record deleted'}
    else:
        result = {'message': 'no record found'}
        
    return jsonify({'result':result})


if __name__=='__main__':
    app.run(debug=True)
