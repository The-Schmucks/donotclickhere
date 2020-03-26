import flask
from flask import request, jsonify
import os
from Kadogo import Kadogo

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["ALLOWED_HOSTS"] = ['*']


@app.route("/", methods=['GET'])
def home():
    """Present some documentation"""
    return "<h1>Kadogo</h1><p>A prototype API for Kadogo.</p>"

@app.route('/api/v1', methods=['GET'])
def api():
    if 'command' in request.args:
        command = str(request.args['command'])
        ask = Kadogo()
        return ask.api(command)
    else:
        return "Error: No command field provided. Please specify command."
app.run(host= '0.0.0.0')