from flask import Flask, request, jsonify
from io import StringIO
import json
from Client import Client
app = Flask(__name__)
client = Client()

@app.route('/mstAlgo', methods=['POST'])
def test():
    if request.method == 'POST':
        coordinateDict = request.json
        MST = client.createMSTWithCoordinates(coordinateDict)
        finalOrderedArray = client.returnFinalOrderedArray(MST)
        return jsonify(finalOrderedArray)
@app.route('/')
def new():
    return 'Hi there'
