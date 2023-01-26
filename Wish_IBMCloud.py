import json
from flask import Flask, request, jsonify
import random
import asyncio
app = Flask(__name__)


nutzer = 0
newKey=""

api = 0

redirections = 0

requestVal = 0
limVal=10

limits = {'lim1': limVal, 'lim2': limVal, 'lim3': limVal, 'limTot': 28}

async def increaseLimit():
    while True:
        if limits['lim1']<10:
            limits['lim1'] = limits['lim1']+1
        if limits['lim2']<10:
            limits['lim2'] = limits['lim2']+1
        if limits['lim3']<10:
            limits['lim3'] = limits['lim3']+1
        if limits['limTot']<10:
            limits['limTot'] = limits['limTot']+1
        if newKey in limits.keys():
            if limits[newKey]<30:
                limits[newKey] = limits[newKey]+1
        await asyncio.sleep(2)

@app.route('/jobs', methods=['GET', 'PUT', 'POST', 'DELETE'])
def mainJobs():
        global requestVal
        global path
        requestValue(2)
        process()
        userRateLimiting()
        path='Jobs'
        if redirections == 3:
            return jsonify("Error-Request to big")
                
    #    if limit1 <= 0 or limit2 <= 0 or limit3 <= 0 or limitTot <= 0 :
    #        return jsonify('Error-Limit has been reached')
        if limits[newKey] > 30:
            return jsonify("Error-too many request")
        return jsonify({'api: ': api,
        'limit1:': limits['lim1'],
        'limit2: ': limits['lim2'],
        'limit3: ': limits['lim3'],
        'limitTot:': limits['limTot'], 
        'Request value: ': requestVal, 
        'Your Token:': newKey, 
        'Limit-User': limits[newKey],
        'Path': path })

@app.route('/apps', methods=['GET', 'PUT', 'POST', 'DELETE'])
def mainApps():
    global requestVal
    global path
    requestValue(1)
    process()
    userRateLimiting()
    path='Apps'
    if redirections == 3:
        return jsonify("Error-Request to big")
               
#    if limit1 <= 0 or limit2 <= 0 or limit3 <= 0 or limitTot <= 0 :
#        return jsonify('Error-Limit has been reached')
    if limits[newKey] > 30:
        return jsonify("Error-too many request")
    return jsonify({'api: ': api,
    'limit1:': limits['lim1'],
    'limit2: ': limits['lim2'],
    'limit3: ': limits['lim3'],
    'limitTot:': limits['limTot'], 
    'Request value: ': requestVal, 
    'Your Token:': newKey, 
    'Limit-User': limits[newKey],
    'Path': path })

@app.route('/project', methods=['GET', 'PUT', 'POST', 'DELETE'])
def mainProject():
    global requestVal
    global path
    requestValue(3)
    process()
    userRateLimiting()
    path = 'Projects'
    if redirections == 3:
        return jsonify("Error-Request to big")
               
#    if limit1 <= 0 or limit2 <= 0 or limit3 <= 0 or limitTot <= 0 :
#        return jsonify('Error-Limit has been reached')
    if limits[newKey] <= 0:
        return jsonify("Error-too many request")

    return jsonify({'api: ': api,
    'limit1:': limits['lim1'],
    'limit2: ': limits['lim2'],
    'limit3: ': limits['lim3'],
    'limitTot:': limits['limTot'], 
    'Request value: ': requestVal, 
    'Your Token:': newKey, 
    'Limit-User': limits[newKey],
    'Path': path })

@app.route('/reset', methods=['GET', 'PUT', 'POST', 'DELETE'])
def reset():
    global limits
    global limits
    path = 'reset'
    limits = {'lim1': limVal, 'lim2': limVal, 'lim3': limVal, 'limTot': 28}
    limits = {}
    return jsonify({'api: ': api,
    'limit1:': limits['lim1'],
    'limit2: ': limits['lim2'],
    'limit3: ': limits['lim3'],
    'limitTot:': limits['limTot'], 
    'Request value: ': requestVal, 
    'Your Token:': newKey, 
    'Limit-User': limits[newKey],
    'Path': path,})


def requestValue(x):
    global requestVal
    if (request.method == 'GET' or request.method == 'DELETE'):
        requestVal=1
    if (request.method == 'PUT' or request.method == 'POST'):
        requestVal=2
    requestVal=requestVal*x

def process():
    global api
    global redirections
    global requestVal

    api = random.randint(1,3)
    x=0

    if api == 1:
        x = limits['lim1']

    if api == 2:
        x = limits['lim2']

    if api == 3:
        x = limits['lim3']

    if x-requestVal >= 0:
        x=x-requestVal
        limits['limTot']=limits['limTot']-requestVal
        redirections=0
    else:
        if limits['limTot'] > 0:
            if api==1:
                api = random.randint(2,3)
            if api==2:
                api = random.randrange(1,4,2)
            if api==3:
                api = random.randint(1,2)
            redirections=redirections+1
    if api == 1:
        limits['lim1'] = x

    if api == 2:
         limits['lim2'] = x

    if api == 3:
        limits['lim3'] = x

def userRateLimiting():
    global newKey
    data = request.json
    newKey = data['token']
    print(newKey)
    print(type(newKey))
    if newKey in limits.keys():
        limits[newKey] = limits[newKey]-requestVal
    else:
        limits[newKey] = 30
    print(data)

async def increaseLimit():
    while True:
        if limits['lim1']<10:
            limits['lim1'] = limits['lim1']+1
        if limits['lim2']<10:
            limits['lim2'] = limits['lim2']+1
        if limits['lim3']<10:
            limits['lim3'] = limits['lim3']+1
        if limits['limTot']<10:
            limits['limTot'] = limits['limTot']+1
        if newKey in limits.keys():
            if limits[newKey]<30:
                limits[newKey] = limits[newKey]+1
        await asyncio.sleep(2)




app.run(debug=True) 