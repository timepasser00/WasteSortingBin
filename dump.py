# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode


def start():
    # Start PWM running, with value of 0 (pulse off)
    GPIO.setmode(GPIO.BOARD)

    # Set pin 19 as an output, and define as servo1 as PWM pin
    GPIO.setup(19,GPIO.OUT)
    servo1 = GPIO.PWM(19,50) # pin 11 for servo1, pulse 50Hz
    servo1.start(0)

    delay = 0.1
    for i in range(13):
        servo1.ChangeDutyCycle(i)
        time.sleep(delay)
    time.sleep(0.5)
    for i in range(12,0,-1):
        servo1.ChangeDutyCycle(i)
        time.sleep(delay)
    time.sleep(1)
    #servo1.ChangeDutyCycle(2)
    #time.sleep(0.5)
    servo1.ChangeDutyCycle(0)

    # finally:
        #Clean things up at the end
    servo1.stop()
    # GPIO.cleanup()
    # print("Goodbye!")

# start()
# GPIO.cleanup()
