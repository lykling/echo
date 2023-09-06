import json
import logging
import re
from flask import Flask
from flask import request

app = Flask(__name__)
logging.root.setLevel(logging.DEBUG)


@app.route('/healthcheck')
def healthcheck():
    """helthcheck
    """
    return ""


@app.route('/hello')
def hello():
    """hello
    """
    return "Hello World"


@app.route('/getip')
def getip():
    """getip
    """
    client_addr = request.remote_addr
    if 'X-Forwarded-For' in request.headers:
        x_forwarded_for = request.headers.getlist('X-Forwarded-For')
        client_addr = re.split(r',\s*', x_forwarded_for[0])[0]
    elif 'X-Real-IP' in request.headers:
        real_ip = request.headers.getlist('X-Real-IP')
        client_addr = re.split(r',\s*', real_ip[0])[0]
    return client_addr


@app.before_request
def router_in():
    """router_in
    """
    logging.info(json.dumps(list(request.headers.items())))
