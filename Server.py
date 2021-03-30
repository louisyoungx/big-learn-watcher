from flask import Flask
import json
from Core import running
from Log import log

app = Flask(__name__)

running()

@app.route('/')
def getLogData():
    data = log.log_data()
    return jsonify(data)
