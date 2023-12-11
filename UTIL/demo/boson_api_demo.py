# This is a API for BOSON Camera

import sys
sys.path.append("..")
import cv2
import os
import platform
import serial
# from BosonCamAPI import BosonCamAPI
from BosonCamAPI import *
import threading
import time

# palette Info
palette = {0:'WHITEHOT', 1:'BLACKHOT', 2:'RAINBOW', 3:'RAINBOW_HC', 4:'IRONBOW'
         , 5:'LAVA', 6:'ARCTIC', 7:'GLOBOW', 8:'GRADEDFIRE', 9:'HOTTEST',}

# SET PORT Number Setting
CAM = BosonCamAPI(portNum = 'COM4')
# CAM.conn()


# SET VideoCapture index Setting
cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

if not cap.isOpened():
    print("Error: Camera not opened.")
    exit()

window_name = "palette_window"

while True:
    stream_ret, frame = cap.read()
    FPS = f"FPS : {CAM.sysctrlGetCameraFrameRate()}" # Get Camera FPS 
    if stream_ret:
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(1)
        if 48 <= key <= 57:  # range : 0 ~ 9
            number = key - 48
            CAM.colorLutSetId(number)
            cv2.setWindowTitle(window_name, f"{FPS}  //  PALETTE : {palette[number]}")
        if key == ord('q'):
            break