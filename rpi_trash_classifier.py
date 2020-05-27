# ------------------------------------------------------------------------
# Trash Classifier ML Project
# Please review ReadMe for instructions on how to build and run the program
# 
# (c) 2020 by Jen Fox, Microsoft
# MIT License
# --------------------------------------------------------------------------


#import Pi GPIO library button class
from gpiozero import Button, LED, PWMLED
from picamera import PiCamera
from time import sleep

from lobe import ImageModel

#Create input, output, and camera objects
button = Button(2)

yellow_led = LED(17) #garbage
blue_led = LED(27) #recycle
green_led = LED(22) #compost
red_led = LED(23) #hazardous waste facility
white_led = PWMLED(24) #Status light and retake photo

camera = PiCamera()

# Load Lobe TF model
# --> Change model file path as needed
model = ImageModel.load('/home/pi/Lobe/model')

# Take Photo
def take_photo():
    # Quickly blink status light
    white_led.blink(0.1,0.1)
    sleep(2)
    print("Pressed")
    white_led.on()
    # Start the camera preview
    camera.start_preview(alpha=200)
    # wait 2s or more for light adjustment
    sleep(3) 
    # Optional image rotation for camera
    # --> Change or comment out as needed
    camera.rotation = 270
    #Input image file path here
    # --> Change image path as needed
    camera.capture('/home/pi/Pictures/image.jpg')
    #Stop camera
    camera.stop_preview()
    white_led.off()
    sleep(1)

# Identify prediction and turn on appropriate LED
def led_select(label):
    print(label)
    if label == "garbage":
        yellow_led.on()
        sleep(5)
    if label == "recycle":
        blue_led.on()
        sleep(5)
    if label == "compost":
        green_led.on()
        sleep(5)
    if label == "hazardous waste facility":
        red_led.on()
        sleep(5)
    if label == "not trash!":
        white_led.on()
        sleep(5)
    else:
        yellow_led.off()
        blue_led.off()
        green_led.off()
        red_led.off()
        white_led.off()

# Main Function
while True:
    if button.is_pressed:
        take_photo()
        # Run photo through Lobe TF model
        result = model.predict_from_file('/home/pi/Pictures/image.jpg')
        # --> Change image path
        led_select(result.prediction)
    else:
        # Pulse status light
        white_led.pulse(2,1)
    sleep(1)
