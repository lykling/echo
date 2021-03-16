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
    return request.remote_addr
