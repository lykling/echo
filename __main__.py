from gevent.pywsgi import WSGIServer
from app import app

server = WSGIServer(('', 8000), app)
server.serve_forever()
