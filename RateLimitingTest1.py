#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
import random
app = Flask(__name__)

global api
api = 0

limVal = 10

limit1 = limVal
limit2 = limVal
limit3 = limVal

limitTot = 28

@app.route('/', methods=['GET'])
@app.route('/', methods=['PUT'])
@app.route('/', methods=['POST'])
@app.route('/', methods=['DELETE'])

  

def main():
    global api
    global limitTot
    global limit1
    global limit2
    global limit3

    requestVal = random.randint(1,3)
    if (request.method == 'PUT' or request.method == 'POST'):
        requestVal=requestVal*2
    
    api = random.randint(1,3)
    
    

    if api == 1:
        limit1= limit1-requestVal
        limitTot= limitTot-requestVal

    if api == 2:
        limit2= limit2-requestVal
        limitTot= limitTot-requestVal

    if api == 3:
        limit3 = limit3-requestVal
        limitTot= limitTot-requestVal

    if limit1 <= 0 or limit2 <= 0 or limit3 <= 0 or limitTot <= 0 :
        return jsonify('Error-Limit has been reached')
        
            
    return jsonify('api: ',api,'limit1:', limit1,'limit2: ', limit2,'limit3: ', limit3,'limitTot:', limitTot, requestVal)



app.run(debug=True)   