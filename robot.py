#!/usr/bin/env python
import time
from buildhat import Motor

# Software Limitatons ~ Spooky!
SPEED = 20

MAX_RIGHT = 90 # POSITION VS DEGREE
MAX_LEFT = -90

MAX_UP = 80
HEAD_POS = 10
MAX_DOWN = -10

class Robot:
    def __init__(self):

        print(f"setting up robot")

        self.flippy = 1

        self.x = Motor('C')
        self.y = Motor('D')

        print(f"Motor X Connected? : {self.x.connected}")
        print(f"Motor Y Connected? : {self.y.connected}")

        self.x.set_default_speed(SPEED)
        self.y.set_default_speed(SPEED)

        print("DONE")

#    def __del__(self):
#        print("i am being destroyed, goodbye cruel world")

    def Patrol(self):
        self.x.run_to_position(MAX_RIGHT)
        self.x.run_to_position(MAX_LEFT)


    def MotorHandlerX(self,speed, pos, apos): # MIGHT BE TRASH?
        print(f"MOTOR X position: {pos}\t")
        if pos > 90 or pos < -90:
            self.x.stop()
            print("MOTOR X STOPPED! TOO FAR!")

    def MotorHandlerY(self,speed, pos, apos):
        print(f"MOTOR Y position: {pos}\t")
        if pos > 45 or pos < -10:
            self.y.stop()
            print("MOTOR Y STOPPED! TOO FAR!")

    def GetPositions(self):
        return [self.x.get_position(),self.y.get_position()]





