#main.py
from gevent import monkey
from random import *
monkey.patch_all()

import time
from threading import Thread
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, disconnect
import serial

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None
#ser = serial.Serial('/dev/tty.usbserial-141',9600)

def loop_forever():
    #read_byte = ser.read(2)
    socketio.emit('message', {'data': 'This is data', 'time': read_byte.decode('ascii')}, namespace='/test')
    while read_byte is not None:
	#read_byte = ser.read(2)
        socketio.emit('message', {'data': 'This is data', 'time': read_byte.decode('ascii')}, namespace='/test')
	print read_byte.decode("ascii")

def background_stuff():
     """ python code in main.py """
     print('In background_stuff')
     while True:
        time.sleep(1)
        print("sleeping")
        t = str(randint(40,90))
        socketio.emit('message', {'data': 'This is data', 'time': t}, namespace='/test')

@app.route('/lib/<path:path>')
def send_js(path):
   return app.send_static_file('lib/'+path)

@app.route('/styles/<path:path>')
def send_styles(path):
   return app.send_static_file('styles/'+path)

@app.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_stuff)
        thread.start()
    return app.send_static_file('index.html')

mqttThread = Thread(target=loop_forever)
mqttThread.start()


app.run()
# from flask import Flask, request
# # set the project root directory as the static folder, you can set others.
# app = Flask(__name__)
#
# @app.route('/')
# def root():
#     return app.send_static_file('index.html')
# app.run()
