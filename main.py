#!/usr/bin/env python

from flask import Flask
from flask import abort
from flask import request
app = Flask(__name__)

@app.route("/version", methods=['GET'])
def version():
    if request.method == 'GET':
       return "0.1"
    else:
        abort(404)

if __name__ == "__main__":
    app.run(port=11123)

