import time
from Motor import *
import RPi.GPIO as GPIO
class Line_Tracking:
    def __init__(self):  #automatically called, assign values/operations
        self.leftIR = 14
        self.middleIR = 15
        self.rightIR = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.leftIR,GPIO.IN)
        GPIO.setup(self.middleIR,GPIO.IN)
        GPIO.setup(self.rightIR,GPIO.IN)
    def run(self):
        while True:
            LMR=0x00
            if GPIO.input(self.leftIR)==True:
                self.LMR=(self.LMR | 4)
            if GPIO.input(self.middleIR)==True:
                self.LMR=(self.LMR | 2)
            if GPIO.input(self.rightIR)==True:
                self.LMR=(self.LMR | 1)
            if self.LMR==2:
                PWM.setMotorModel(800,800,800,800)
            elif self.LMR==4:
                PWM.setMotorModel(-1500,-1500,2500,2500)
            elif self.LMR==6:
                PWM.setMotorModel(-2000,-2000,4000,4000)
            elif self.LMR==1:
                PWM.setMotorModel(2500,2500,-1500,-1500)
            elif self.LMR==3:
                PWM.setMotorModel(4000,4000,-2000,-2000)
            elif self.LMR==7:
                #pass
                PWM.setMotorModel(0,0,0,0)
                break

#(x,x,x,x) = (leftfront, leftrear, rightfront, rightrear)

infrared=Line_Tracking()

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        infrared.run()
    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
