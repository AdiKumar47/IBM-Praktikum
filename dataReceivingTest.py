import json
from flask import Flask, request, jsonify
app = Flask(__name__)
count = 0

token = []
@app.route('/', methods=['GET'])
@app.route('/', methods=['PUT'])
@app.route('/', methods=['DELETE'])


@app.route('/', methods=[ 'POST'])
def parse_request():
    data = request.json
    token.append(data)
    count = token.count(data)
    if count >30:
        return jsonify("error")
    return jsonify(count)
    

app.run(debug=True)
