#!/usr/bin/env python
import time
from buildhat import Motor

# Software Limitatons ~ Spooky!
SPEED = 10

MAX_RIGHT = 90
MAX_LEFT = -90

MAX_UP = 80
HEAD_POS = 10
MAX_DOWN = -10

DEBUG = 1

class Robot:
    def __init__(self):

        print(f"setting up robot")

        self.flippy = 1
        self.xPosition = 0
        self.yPosition = 0

        self.x = Motor('C')
        self.y = Motor('D')

        self.x.set_default_speed(SPEED)
        self.y.set_default_speed(SPEED)

        self.x.when_rotated = self.MotorHandlerX 
        self.y.when_rotated = self.MotorHandlerY

        self.InitialAlign()
           
        print(f"finished setup")

    def Patrol(self):
        self.x.run_to_position(MAX_RIGHT)
        self.x.run_to_position(MAX_LEFT)


    def MotorHandlerX(self,speed, pos, apos): # MIGHT BE TRASH?
        print(f"MOTOR X position: {pos}\t")
        if pos > 90 or pos < -90:
            self.x.stop()
            print("MOTOR X STOPPED! TOO FAR!")
        self.xPosition = pos

    def MotorHandlerY(self,speed, pos, apos):
        print(f"MOTOR Y position: {pos}\t")
        if pos > 45 or pos < -45:
            self.y.stop()
            print("MOTOR Y STOPPED! TOO FAR!")
        self.yPosition = pos

    def InitialAlign(self):
        #FIX ME DIRECTION = clockwise or counter if how fucked up it is!
        self.x.run_to_position(0)
        self.y.run_to_position(HEAD_POS)
        self.y.run_to_position(MAX_DOWN)
        self.y.run_to_position(HEAD_POS)
        self.x.run_to_position(MAX_RIGHT)
        self.x.run_to_position(0)
        self.x.run_to_position(MAX_LEFT)
        self.x.run_to_position(0)
        self.y.run_to_position(MAX_UP)
        self.y.run_to_position(HEAD_POS)
        self.y.run_to_position(MAX_DOWN)
        self.y.run_to_position(HEAD_POS)

    def GetPosition(self):
        return {self.x.get_position(),self.y.get_position()}

    def GoRight(self):
        print("GOING RIGHT")
        self.x.start(5)
        self.x.stop()




