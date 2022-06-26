# ------------------------------------------------------------------------
# Trash Classifier ML Project - Test script for the usage of PiCamera: file access and camera capture
# Expected behaviour: successfully turns on the camera and captures 6 images during one minute in real time.
# 
# (c) 2020 by Jen Fox, Microsoft
# MIT License
# --------------------------------------------------------------------------

from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Take photo and save as a jpg file (using photoPath as file realpath)
def take_photo(photoPath):
    camera.start_preview(alpha=200)
    sleep(3) 
    camera.rotation = 270
    camera.capture(photoPath)
    camera.stop_preview()

# take a picture and save as a file in /home/pi/Pictures/
for id in range(1,7):
    take_photo("/home/pi/Pictures/image_testing_picamera_id{0}.jpg".format(id))
    sleep(10);