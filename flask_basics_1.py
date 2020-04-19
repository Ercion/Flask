# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:00:08 2020

@author: Ercan Karaçelik
"""

from flask import Flask

'''
The flask object implements a WSGI application and acts as the central object. 
WSGI --> Web Server Gate Interface - is a specificatiın for a universal interface between
the webserver and the web application

'''

app=Flask(__name__)

print(app)


'''
use the route() decorator to tell Flask what URL should trigger our function.


the @app.route() decorator can accept a second argument: a list of accepted HTTP methods. 
Flask views will only accept GET requests by default, 
unless the route decorator explicitly lists which HTTP methods the view should honor.

@app.route("/api/v1/users/", methods=['GET', 'POST', 'PUT'])

'''


@app.route('/')
def hello_world():
    return 'Hello World'


if __name__=='__main__':
    app.run(debug=False)
    

'''

app.run(host,port,debug,options)

host --> default 127.0.0.1
port -->default 5000
debug --> default False

'''