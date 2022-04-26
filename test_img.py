 # import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
# initialize the camera and grab a reference to the raw camera capture
def click():
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)
    # # allow the camera to warmup
    time.sleep(0.1)
    # # grab an image from the camera
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    # # saves the image 
    cv2.imwrite("test_img.jpg",image)
    camera.close()
    # sys.exit()

# click()
