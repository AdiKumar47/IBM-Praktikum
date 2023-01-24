#https://pythonbasics.org/flask-rest-api/
#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
@app.route('/', methods=['POST'])
@app.route('/', methods=['DELETE'])
@app.route('/', methods=['PUT'])
def index():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})

app.run()