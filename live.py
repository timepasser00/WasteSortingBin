from http.client import GATEWAY_TIMEOUT
import my_pred
import RPi.GPIO as GPIO
import time
sensor = 37
rnd = 10
try:
    while(rnd):
        # rnd = rnd - 1
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(sensor, GPIO.IN)
        state = GPIO.input(sensor)
        # if state < 1:
        #     state = 0
        # print(state)
        if state == True:
            print("nothing detected")
            time.sleep(1)
        else:
            print("waste detectd")
            # time.sleep(2)
            # b_7.start()
            my_pred.start()
            time.sleep(1)
            # b_7.start()
except KeyboardInterrupt:
    print("You've exited the program")
finally:
    GPIO.cleanup()

    
