#coding=utf-8

import cv2
import os
import subprocess
import time


def detectFaces(image_name):
    img = cv2.imread(image_name)
    face_cascade = cv2.CascadeClassifier("/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml")
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img #if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)#1.3和5是特征的最小、最大检测窗口，它改变检测结果也会改变
    result = []
    for (x,y,width,height) in faces:
        result.append((x+width/2,y+height/2,width,height))
    return result


def loop():
    tmpfile = '232412tmp.jpg'
    subprocess.call(["raspistill","-w","400","-h","400","-e","jpg","-n","-t","1","-o",tmpfile])
    faces = detectFaces(tmpfile)
    for i in range(0, len(faces), 1):
        print(faces[i])
    os.remove(tmpfile)
    time.sleep(1)

if __name__ == '__main__':
    loop()
