from flask import Flask
import json
from Core import core
from Log import log

app = Flask(__name__)

core()

@app.route('/')
def getLogData():
    data = json.dumps(log.get_data())
    return data
