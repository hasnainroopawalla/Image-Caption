from flask import Flask,flash,jsonify,request,render_template,redirect,url_for
from PIL import Image
import numpy
import cv2
import time
import werkzeug
import os

app = Flask(__name__)

objs = []

@app.route("/")
def firstpage():
    global objs
    return render_template('index.html',objs=objs)

@app.route("/getobjects",methods=["GET", "POST"])
def objectdetection():
    import maskrcnn
    import yolo
    global objs
    file = request.files['file']
    inputimg = Image.open(file).convert('RGB')
    img = numpy.array(inputimg)

    print()
    start = time.time()
    maskrcnn_objs = maskrcnn.getobj(img)
    end = time.time()
    print('\nMask-RCNN:')
    print(maskrcnn_objs)
    print('Time:',end-start)
    print()
    masktime = (end-start)
    
    start = time.time()
    yolo_objs = yolo.getobj(img)
    end = time.time()
    print('YOLO V3:')
    print(yolo_objs)
    print('Time:',end-start)
    print()
    yolotime = (end-start)
    print("test")
    print(yolotime)
    print(masktime)
    # maskout = cv2.imread('static/images/maskrcnn_out.png')
    # yoloout = cv2.imread('static/images/yolo_out.png')
    # return render_template('display.html',maskout=maskout, yoloout=yoloout)


    return render_template('display.html',yolotime=yolotime,masktime=masktime)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=5000, debug=True)