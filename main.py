#!/usr/bin/env python
import cv2, sys, time, os
from robot import Robot

MAX_RIGHT = 80
MAX_LEFT = -80
MAX_UP = 45
MAX_DOWN = -45

# Load the BCM V4l2 driver
os.system('sudo modprobe bcm2835-v4l2')
os.system('v4l2-ctl -p 40')

FRAME_W = 320
FRAME_H = 200

cascPath = '/usr/share/opencv/lbpcascades/lbpcascade_frontalface.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  FRAME_W);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_H);
time.sleep(2)

rob = Robot()

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, -1)
    
    if ret == False:
      print("Error getting image")
      continue

    # Convert to greyscale for easier+faster+accurate face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist( gray )

    # Do face detection to search for faces from these captures frames
    faces = faceCascade.detectMultiScale(frame, 1.1, 3, 0, (10, 10))
    
        
    #Below draws the rectangle onto the screen then determines how to move the camera module so that the face can always be in the centre of screen. 

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (18, 255, 18), 4)
        # center of face
        x = x + (w/2)
        y = y + (h/2)
        
        
        # x axis
        if x<((FRAME_W/2)-5) and rob.xPosition > MAX_LEFT + 15:
            print("MOVING LEFT")
            print(rob.xPosition)
            rob.x.start(-4)
            if rob.xPosition <= MAX_LEFT:
                rob.x.stop()

        elif x>((FRAME_W/2)+5) and rob.xPosition < MAX_RIGHT - 15:
            print("MOVING RIGHT")
            print(rob.xPosition)
            rob.x.start(4)
            if rob.xPosition >= MAX_RIGHT:
                rob.x.stop()

        else:
            rob.x.stop()

        # y axis
        if y<((FRAME_H/2)-5) and rob.yPosition < MAX_UP - 15:
            print("MOVING UP")
            print(rob.yPosition)
            rob.y.start(4)
            if rob.yPosition >= MAX_UP:
                rob.y.stop()

        elif y>((FRAME_H/2)+5) and rob.yPosition > MAX_DOWN + 5:
            print("MOVING DOWN")
            print(rob.yPosition)
            rob.y.start(-4)
            if rob.yPosition <= MAX_DOWN + 10:
                rob.y.stop()

        else:
            rob.y.stop()

        break
    
    # setup frame
    frame = cv2.resize(frame, (540,300))
    frame = cv2.flip(frame, 1)
   
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

rob.y.stop()
rob.x.stop()
#video_capture.release()
cv2.destroyAllWindows()
