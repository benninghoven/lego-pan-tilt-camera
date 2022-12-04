import cv2, sys, time, os
from robot import Robot

RUNNING = 1
FPS = 60
sleepTime = 1/FPS
COLOR = (18,255,18)
X_SHFT_AMNT = 20
Y_SHFT_AMNT = 10

X_SPEED = 5
Y_SPEED = 3

# Load the BCM V4l2 driver
os.system('sudo modprobe bcm2835-v4l2')
#os.system('v4l2-ctl -p 40')
os.system('v4l2-ctl -p 60')

FRAME_W = 320
FRAME_H = 200

cascPath = '/usr/share/opencv/lbpcascades/lbpcascade_frontalface.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  FRAME_W);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_H);

rob = Robot()

while RUNNING:
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
        cv2.rectangle(frame, (x, y), (x+w, y+h), COLOR, 4)
        # center of face
        x = x + (w/2)
        y = y + (h/2)

        # CENTER X 160 Y 100
        #print(f"X: {x}\tY: {y}")

        # x axis
        if x < FRAME_W/2 + X_SHFT_AMNT and x > FRAME_W/2 - X_SHFT_AMNT:
            rob.x.stop()
            #print("X: IN THE MONEY")
        elif x > FRAME_W/2:
            rob.x.start(X_SPEED*1)
            #print("MOVING RIGHT")
        elif x < FRAME_W/2:
            rob.x.start(X_SPEED*-1)
            #print("MOVING LEFT")
        # y axis
        if y < FRAME_H/2 + Y_SHFT_AMNT and y > FRAME_H/2 - Y_SHFT_AMNT:
            #print("Y: IN THE MONEY")
            rob.y.stop()
        elif y < FRAME_H/2:
            print("MOVING UP")
            rob.y.start(Y_SPEED)
        elif y > FRAME_H/2:
            print("MOVING DOWN")
            rob.y.start(Y_SPEED*-1)
        break

    # setup frame
    frame = cv2.resize(frame, (540,300))
    frame = cv2.flip(frame, 1)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) == ord('q'):
        print("closing application...")
        RUNNING = 0
#    time.sleep(sleepTime)

cv2.destroyAllWindows()
