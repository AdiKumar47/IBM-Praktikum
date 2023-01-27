import json
from flask import Flask, request, jsonify
import random
from threading import Thread
import time
app = Flask(__name__)

global resetTrue
resetTrue = False

nutzer = 0
newKey = ""

api = 0

redirections = 0

requestVal = 0
limVal = 10

jsonFile = open('./Data1.json')
fileData = json.load(jsonFile)
config = fileData
print(config)


@app.route('/jobs', methods=['GET', 'PUT', 'POST', 'DELETE'])
def mainJobs():
    global requestVal
    global path
    requestValue(config['reqValJobs'])
    process()
    userRateLimiting()
    path = 'Jobs'
    if redirections == 3:
        return jsonify("Error-Request to big")
    if config['limTot'] == 0:
        return jsonify('Error-our limits have been reached')
    if config[newKey] <= 0:
        return jsonify("Error-too many request")
    return jsonify({'Instance': api,
                    'limit1': config['lim1'],
                    'limit2': config['lim2'],
                    'limit3': config['lim3'],
                    'limitTot': config['limTot'],
                    'Request value': requestVal,
                    'Your Token': newKey,
                    'Limit-User': config[newKey],
                    'Path': path})


@app.route('/apps', methods=['GET', 'PUT', 'POST', 'DELETE'])
def mainApps():
    global requestVal
    global path
    requestValue(config['reqValApps'])
    process()
    userRateLimiting()
    path = 'Apps'
    if redirections == 3:
        return jsonify("Error-Request to big")
    if config['limTot'] == 0:
        return jsonify('Error-our limits have been reached')
    if config[newKey] <= 0:
        return jsonify("Error-too many request")
    return jsonify({'Instance': api,
                    'limit1': config['lim1'],
                    'limit2': config['lim2'],
                    'limit3': config['lim3'],
                    'limitTot': config['limTot'],
                    'Request value': requestVal,
                    'Your Token': newKey,
                    'Limit-User': config[newKey],
                    'Path': path})


@app.route('/project', methods=['GET', 'PUT', 'POST', 'DELETE'])
def mainProject():
    global requestVal
    global path
    requestValue(config['reqValProjects'])
    process()
    userRateLimiting()
    path = 'Projects'
    if redirections == 3:
        return jsonify("Error-Request to big")
    if config['limTot'] == 0:
        return jsonify('Error-our limits have been reached')
    if config[newKey] <= 0:
        return jsonify("Error-too many request")

    return jsonify({'Instance': api,
                    'limit1': config['lim1'],
                    'limit2': config['lim2'],
                    'limit3': config['lim3'],
                    'limitTot': config['limTot'],
                    'Request value': requestVal,
                    'Your Token': newKey,
                    'Limit-User': config[newKey],
                    'Path': path})


@app.route('/reset', methods=['GET', 'PUT', 'POST', 'DELETE'])
def reset():
    global config
    global config
    path = 'reset'
    jsonFile = open('./Data1.json')
    fileData = json.load(jsonFile)
    config = fileData
    return jsonify({'Instance': api,
                    'limit1': config['lim1'],
                    'limit2': config['lim2'],
                    'limit3': config['lim3'],
                    'limitTot': config['limTot'],
                    'Request value': requestVal,
                    'Path': path, })


def requestValue(x):
    global requestVal
    if (request.method == 'GET'):
        requestVal = config['reqValGet']
    if (request.method == 'DELETE'):
        requestVal = config['reqValDel']
    if (request.method == 'PUT'):
        requestVal = config['reqValPut']
    if (request.method == 'POST'):
        requestVal = config['reqValPost']

    requestVal = requestVal*x


def process():
    global api
    global redirections
    global requestVal

    api = random.randint(1, 3)
    x = 0

    if api == 1:
        x = config['lim1']

    if api == 2:
        x = config['lim2']

    if api == 3:
        x = config['lim3']

    if x - int(requestVal) >= 0:
        print(x)
        print(requestVal)
        x = x - int(requestVal)
        config['limTot'] = config['limTot']-requestVal
        redirections = 0
    else:
        if config['limTot'] > 0:
            if api == 1:
                api = random.randint(2, 3)
            if api == 2:
                api = random.randrange(1, 4, 2)
            if api == 3:
                api = random.randint(1, 2)
            redirections = redirections+1
    if api == 1:
        config['lim1'] = x

    if api == 2:
        config['lim2'] = x

    if api == 3:
        config['lim3'] = x


def userRateLimiting():
    global newKey
    data = request.json
    newKey = data['token']
    print(newKey)
    print(type(newKey))
    if newKey in config.keys():
        config[newKey] = config[newKey]-requestVal
    else:
        config[newKey] = config['limMaxUser']-1
    print(data)


def increaseLimit():
    while True:
        if config['lim1'] < 10:
            config['lim1'] = config['lim1']+1
        if config['lim2'] < 10:
            config['lim2'] = config['lim2']+1
        if config['lim3'] < 10:
            config['lim3'] = config['lim3']+1
        if config['limTot'] < 28:
            config['limTot'] = config['limTot']+3
        if newKey in config.keys():
            if config[newKey] < config['limMaxUser']:
                config[newKey] = config[newKey]+3
        time.sleep(config['regTime'])


if __name__ == '__main__':
    thread = Thread(target=increaseLimit)
    thread.daemon = True
    thread.start()
    app.run(debug=True)
