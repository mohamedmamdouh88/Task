#!/usr/bin/env python
"""
mascot: a microservice for serving mascot data
"""
import json
from flask import Flask, jsonify, abort, make_response

APP = Flask(__name__)

@APP.route('/', methods=['GET'])
def get_mascots():
    return "Mohamed"
    
if __name__ == '__main__':
    APP.run("0.0.0.0", port=8080, debug=True)
