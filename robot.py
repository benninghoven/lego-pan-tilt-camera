#!/usr/bin/env python
import time
from buildhat import Motor

# Software Limitatons ~ Spooky!
SPEED = 10
MAX_RIGHT = 80
MAX_LEFT = -80
MAX_UP = 80
MAX_DOWN = 0
HEAD_POS = 10
SHIFT_AMNT = 8

DEBUG = 1

class Robot:
    def __init__(self):

        self.debounce = False

        self.name = "K.Y.L.E"
        print(f"setting up {self.name}")

        self.flippy = 1

        self.xPosition = 0
        self.yPosition = HEAD_POS

        self.x = Motor('C')
        self.y = Motor('D')

        self.x.set_default_speed(SPEED)
        self.y.set_default_speed(SPEED)

        self.x.when_rotated = self.MotorHandlerX 
        self.y.when_rotated = self.MotorHandlerY

        if DEBUG:
            self.InitialAlign()
           
        print(f"finished setup")

    def Patrol(self):
        self.x.set_default_speed(6)
        for i in range(5):
            self.x.run_to_position(MAX_RIGHT)
            self.x.run_to_position(MAX_LEFT)
        self.x.run_to_position(0)
        self.x.set_default_speed(SPEED)


    def MotorHandlerX(self,speed, pos, apos):
        self.xPosition = pos
        if pos > 90 or pos < -90:
            self.x.stop()
        print(f"MOTOR X position: {pos}\t")

    def MotorHandlerY(self,speed, pos, apos):
        self.yPosition = pos
        if pos > 45 or pos < -45:
            self.y.stop()
        print(f"MOTOR Y position: {pos}\t")

    def InitialAlign(self):
        self.y.run_to_position(MAX_DOWN)
        self.x.run_to_position(MAX_RIGHT)
        self.x.run_to_position(MAX_LEFT)
        self.x.run_to_position(0)
        self.y.run_to_position(MAX_UP)
        self.y.run_to_position(MAX_DOWN)

    def GoLeft(self):
        if self.debounce:
            return
        else:
            self.debounce = True
        self.nextPos_x = self.xPosition - SHIFT_AMNT
        if self.nextPos_x < MAX_LEFT:
            self.nextPos_x = MAX_LEFT
        else:
            self.x.run_to_position(self.nextPos_x)
        self.debounce = False

    def GoRight(self):
        if self.debounce:
            return
        else:
            self.debounce = True
        self.nextPos_x = self.xPosition + SHIFT_AMNT
        if self.nextPos_x > MAX_RIGHT:
            self.nextPos_x = MAX_RIGHT
        else:
            self.x.run_to_position(self.nextPos_x)
        self.debounce = False

    def GoUp(self):
        if self.debounce:
            return
        else:
            self.debounce = True
        self.nextPos_y = self.yPosition + SHIFT_AMNT
        if self.nextPos_y > MAX_UP:
            self.nextPos_y = MAX_UP
        else:
            self.y.run_to_position(self.nextPos_y)
        self.debounce = False

    def GoDown(self):
        if self.debounce:
            return
        else:
            self.debounce = True
        self.nextPos_y = self.yPosition - SHIFT_AMNT
        if self.nextPos_y < MAX_DOWN:
            self.nextPos_y = MAX_DOWN
        else:
            self.y.run_to_position(self.nextPos_y)
        self.debounce = False


    def Test(self):
        for i in range(100):
            print("PATROLLING")
            self.Patrol()











