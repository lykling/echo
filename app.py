from flask import Flask
from flask import request

app = Flask(__name__)


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
        client_addr = x_forwarded_for[0].rpartition(' ')[-1]
    return client_addr
