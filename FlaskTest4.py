#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
global name
name = 'Nikolai'
app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/', methods=['PUT'])
@app.route('/', methods=['POST'])
@app.route('/', methods=['DELETE'])

def get():
    name = 'Nikolai'
    if (request.method=='GET'):
        print(name)
        return jsonify(name)
    if (request.method=='PUT'):
        name = 'ztrcit7vt7futgtzgh7tzgh78u78u'
        return jsonify(name)
app.run(debug=True)