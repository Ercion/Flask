# -*- coding: utf-8 -*-

"""
Created on Sun Apr 24 13:25:08 2020
@author: Ercan Karaçelik
"""

from flask import Flask,request
from flask_restful import Resource, Api


'''

Flask --> The flask object implements a WSGI application and acts as the central object. 
WSGI --> The Web Server Gateway Interface is a simple calling convention for web servers to forward requests to web applications or frameworks
request.get_json --> converts the JSON object into Python data
Resource --> Flask-RESTful provides a Resource base class that can define the routing for one or more HTTP methods for a given URL 
Api --> The main entry point for the application. You need to initialize it with a Flask Application.

'''


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'about':'Hello World!'}

    def post(self):
        some_json=request.get_json()
        return {'you sent ':some_json}, 201


class Multi(Resource):
    def get(self,num):
        num*=10
        return {'return': num}


api.add_resource(HelloWorld,'/')
api.add_resource(Multi,'/multi/<int:num>')


if __name__=='__main__':
    app.run(debug=True,port=5003)