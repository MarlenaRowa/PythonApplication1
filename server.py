"""
To run:

$FLASK_APP="server" flask run -h 0.0.0.0 -p 5011 
 
"""
from flask import Flask, request
from datetime import datetime
import json
app = Flask(__name__)
dt = datetime.now()
jsona = "Dziadek"

@app.route("/notification/versionOnRobot", methods=['GET', 'POST'])
def hello_world():
    print(request.path)
    print(request.method)
    print(request.json)
    print(json.dumps(request.json, indent=4))

    global jsona
    jsona = json.dumps(request.json)

    return ""

@app.route("/test")
def wannacry():
    return jsona
    
@app.route("/test2")
def wannacry2():
    return "Babcia"
    

print (dt)
