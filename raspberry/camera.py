#!/usr/bin/env python3
import microgear.client as netpie
import time
import cv2
import os
import dropbox
key = 'O8cRkrqQUTxs3vV'
secret = '0nfSTqyUHLPF29faaNACpAcox'
app = 'smarth'

netpie.create(key,secret,app,{'debugmode': True})
connected = False

def connection():
 global connected
 connected = True
 print("Connected")
 
def subscription(topic,msg):
 if msg == "yes":
    cupture() 

def cupture () :
    camera = cv2.VideoCapture(0)
    camera.set(3,1920)
    camera.set(4,1080)
    filename = "opencv"+str(time.time())+".jpg"
    for i in range (0,5):
        return_value, image = camera.read()
    cv2.imwrite(filename, image)
    saveImg(filename)
    del(camera)
    os.remove("/home/pi/Desktop/"+filename)
   
def saveImg (filename) :
    dbx = dropbox.Dropbox("cKG3HoKEj5UAAAAAAABN6J8oc2yJIB7q6pDRjVKBNvrX_gs0D0vSSAHCT-QVRnlI")
    dbx.users_get_current_account()
    file_path = os.path.join("/home/pi/Desktop/", filename)
    f = open(file_path, 'rb')
    dbx.files_upload(f.read(),'/cam/'+filename)
    
def callback_error(msg) :
    print(msg)

def callback_reject(msg) :
    print (msg)
    print ("Script exited")
    exit(0)

 
imageWidth = 1280
imageHeight = 720
camera_index = 0
 

this_name = 'CAMERA'     
running = True
ready_to_send = False

netpie.setname(this_name)
netpie.on_reject = callback_reject
netpie.on_connect = connection
netpie.on_message = subscription
netpie.on_error = callback_error
netpie.subscribe("/camera")
netpie.connect(False) 
while True:
  pass


