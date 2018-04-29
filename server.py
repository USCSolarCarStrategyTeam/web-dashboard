#main.py
from gevent import monkey
from random import *
monkey.patch_all()

import time
from threading import Thread
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, disconnect
import serial
import random
from datetime import datetime
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None
#ser = serial.Serial('/dev/tty.usbserial-141',9600)

# ser = serial.Serial(
# 
#    port='/dev/tty.usbserial-1412',
#    baudrate = 9600,
# #    parity=serial.PARITY_NONE,
# #    stopbits=serial.STOPBITS_ONE,
# #    bytesize=serial.EIGHTBITS,
# #    timeout=1
# )

#data1 = ser.readline();

def loop_forever():
    #read_byte = ser.read(2)
    socketio.emit('message', {'data': 'This is data', 'time': read_byte.decode('ascii')}, namespace='/test')
    socketio.emit('message2', {'data2': 'This is data', 'time': read_byte.decode('ascii')}, namespace='/test')
    while read_byte is not None:
		#read_byte = ser.read(2)
        socketio.emit('message', {'data': 'This is data', 'time': read_byte.decode('ascii')}, namespace='/test')
        socketio.emit('message2', {'data2': 'This is data', 'time': read_byte.decode('ascii')}, namespace='/test')
	print read_byte.decode("ascii")
	
	

def background_stuff():

     """ python code in main.py """
     print('In background_stuff')
     random.seed(datetime.now())
     ser = serial.Serial(port='/dev/tty.usbserial-1413',baudrate = 9600)
     myList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
     while True:
     	for z in range(0, 25):
     		data1 = ser.readline();
     		myList[z] = data1;
     	time.sleep(0.25);
     	y = str(randint(-10,10));
     	socketio.emit('message', {'data': 'This is data', 'time': myList}, namespace='/test')
#         socketio.emit('message2', {'data2': 'This is data', 'time': x}, namespace='/test')
        

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

     	#ser = serial.Serial(port='/dev/tty.usbserial-1412',baudrate = 9600)
     	#data1 = ser.readline();
     	#value = int(data1);
     	#counter = counter + 1;
     	# while (counter < 25):
#      		myList[counter] = data1;
#      		counter= counter+1;
        #time.sleep(0.5)
        #print("sleeping")
        #t = str(randint(40,90))
        #t = myList[counter];
        #if counter == 6: counter = 0;
        #for z in range(0, 24):
        	#data1 = ser.readline();
        	#x = str(randint(60,70));
        	#myList[z] = data1;
        	#socketio.emit('message', {'data': 'This is data', 'time': data1}, namespace='/test')
#         for z in range(0, 4):
#         	data1 = ser.readline();
#         	socketio.emit('message', {'data2': 'This is data', 'time': data1}, namespace='/test')
