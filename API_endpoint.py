# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 21:13:30 2021

@author: Tushar
"""

from flask import Flask, jsonify, request, make_response
from flask_httpauth import HTTPBasicAuth
import gevent.pywsgi

auth = HTTPBasicAuth()

app = Flask(__name__)


@auth.get_password
def get_password(username):
    if username == 'automate':
        return '123456789'
    return None

@auth.error_handler
def unauthorized():
    return (jsonify({'error': 'Unauthorized access'}), 401)

@app.route('/', methods = ['GET'])
def index_test():
    return "Api works just fine!!!"
# if __name__ == '__main__':
#     app.run(debug=True)

app_server = gevent.pywsgi.WSGIServer(("0.0.0.0", 4000), app)
app_server.serve_forever()