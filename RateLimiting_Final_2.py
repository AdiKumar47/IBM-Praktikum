#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
import random
import time
import asyncio

app = Flask(__name__)

nutzer = 0
count = {}
global newKey
newkey = ""

api = 0

redirections = 0

requestVal = 0

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
    asyncio.gather(processEverything(), refresh())
    if redirections == 3:
        return jsonify("Error-Request to big")

#    if limit1 <= 0 or limit2 <= 0 or limit3 <= 0 or limitTot <= 0 :
#        return jsonify('Error-Limit has been reached')
    if count[newKey] > 30:
        return jsonify("Error-too many request")

    return jsonify('api: ',
                   api,
                   'limit1:',
                   limit1,
                   'limit2: ',
                   limit2,
                   'limit3: ',
                   limit3,
                   'limitTot:',
                   limitTot,
                   'Request value: ',
                   requestVal,
                   'Your Token:',
                   newKey,
                   'Limit-User',
                   count[newKey])


async def processEverything():
    processApi
    requestValue()
    userRateLimiting()


def processApi():
    global api
    global limitTot
    global limit1
    global limit2
    global limit3
    global redirections
    global requestVal
    global newKey

    api = random.randint(1, 3)
    x = 0

    if api == 1:
        x = limit1

    if api == 2:
        x = limit2

    if api == 3:
        x = limit3

    if x-requestVal > 0:
        x = x-requestVal
        limitTot = limitTot-requestVal
        redirections = 0
    else:
        if limitTot > 0:
            if api == 1:
                api = random.randint(2, 3)
            if api == 2:
                api = random.randrange(1, 4, 2)
            if api == 3:
                api = random.randint(1, 2)
            redirections = redirections+1

    if api == 1:
        limit1 = x

    if api == 2:
        limit2 = x

    if api == 3:
        limit3 = x


def requestValue():
    global requestVal
    requestVal = random.randint(1, 3)
    if (request.method == 'PUT' or request.method == 'POST'):
        requestVal = requestVal*2


def userRateLimiting():
    global newKey
    data = request.json
    newKey = data['token']
    print(newKey)
    print(type(newKey))
    if newKey in count.keys():
        count[newKey] = count[newKey]+requestVal
    else:
        count[newKey] = 1
    print(data)


async def refresh():
    global limitTot
    global limit1
    global limit2
    global limit3
    time.sleep(3)
    if limit1 < 10:
        limit1 = limit1+1
    if limit2 < 10:
        limit2 = limit2+1
    if limit3 < 10:
        limit3 = limit3+1
    if limitTot < 28:
        limitTot = limitTot+3


app.run(debug=True)
