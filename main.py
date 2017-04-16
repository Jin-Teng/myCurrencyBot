#!/usr/bin/env python

from flask import Flask
from flask import abort
from flask import request
app = Flask(__name__)

BOT_TOKEN = ""

@app.route("/fbCallback", methods=['GET', 'POST'])
def fb_cb_handler():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        if token == BOT_TOKEN:
            return request.args.get('hub.challenge')
        else:
            abort(403)
    else:
        abort(405) 

@app.route("/version", methods=['GET'])
def version():
    if request.method == 'GET':
       return "0.1"
    else:
        abort(404)

if __name__ == "__main__":
    app.run(port=11123)

