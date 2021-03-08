import time
from Motor import *
import RPi.GPIO as GPIO
class Line_Tracking:
    def __init__():  #automatically called, assign values/operations
        leftIR = 14
        middleIR = 15
        rightIR = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(leftIR,GPIO.IN)
        GPIO.setup(middleIR,GPIO.IN)
        GPIO.setup(rightIR,GPIO.IN)
    def run():
        while True:
            LMR=0x00
            if GPIO.input(leftIR)==True:
                LMR=(LMR | 4)
            if GPIO.input(middleIR)==True:
                LMR=(LMR | 2)
            if GPIO.input(rightIR)==True:
                LMR=(LMR | 1)
            if LMR==2:
                PWM.setMotorModel(800,800,800,800)
            elif LMR==4:
                PWM.setMotorModel(-1500,-1500,2500,2500)
            elif LMR==6:
                PWM.setMotorModel(-2000,-2000,4000,4000)
            elif LMR==1:
                PWM.setMotorModel(2500,2500,-1500,-1500)
            elif LMR==3:
                PWM.setMotorModel(4000,4000,-2000,-2000)
            elif LMR==7:
                #pass
                PWM.setMotorModel(0,0,0,0)

#(x,x,x,x) = (leftfront, leftrear, rightfront, rightrear)

infrared=Line_Tracking()

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        infrared.run()
    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
