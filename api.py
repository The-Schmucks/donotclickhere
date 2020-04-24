import flask
from flask import request
from Kadogo import Kadogo

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["ALLOWED_HOSTS"] = ['*'] #allows all hosts(applications) to access the api


@app.route("/", methods=['GET']) #sets the home() as index of the api
def home():
    #Present some documentation
    return "<h1>Kadogo</h1><p>A prototype API for Kadogo.</p>"

@app.route('/api/v1', methods=['GET']) #sets the api() as /api/v1 of the api
def api():
    if 'command' in request.args: #chech if a 'command' parameter was passed
        command = str(request.args['command'])
        ask = Kadogo()
        return ask.api(command)
    else:
        return "Error: No command field provided. Please specify command."

app.run(host= '0.0.0.0') #host:0.0.0.0 to open the app to a local network not only on your machine.