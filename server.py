#main.py
from gevent import monkey
from random import *
monkey.patch_all()
import paho.mqtt.client as mqtt

import time
from threading import Thread
from flask import Flask, render_template, session, request
from flask.ext.socketio import SocketIO, emit, join_room, disconnect

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.
    client.subscribe("hello/world")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Topic: ", msg.topic+"\nMessage: "+str(msg.payload))
    socketio.emit('message', {'data': 'This is data', 'time': msg.payload.decode('utf-8')}, namespace='/test')
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

def background_stuff():
     """ python code in main.py """
     print('In background_stuff')
     while True:
         time.sleep(1)
         print("sleeping")
        #  t = str(randint(40,90))
        #  socketio.emit('message', {'data': 'This is data', 'time': t}, namespace='/test')

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

mqttThread = Thread(target=client.loop_forever)
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
