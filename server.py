#main.py
from gevent import monkey
monkey.patch_all()

import time
from threading import Thread
from flask import Flask, render_template, session, request
from flask.ext.socketio import SocketIO, emit, join_room, disconnect

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None

def background_stuff():
     """ python code in main.py """
     print('In background_stuff')
     while True:
         time.sleep(1)
         print("sleeping")
         t = str(time.clock())
         socketio.emit('message', {'data': 'This is data', 'time': t}, namespace='/test')

@app.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_stuff)
        thread.start()
    return app.send_static_file('index.html')

app.run()
# from flask import Flask, request
# # set the project root directory as the static folder, you can set others.
# app = Flask(__name__)
#
# @app.route('/')
# def root():
#     return app.send_static_file('index.html')
# app.run()
