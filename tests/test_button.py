# ------------------------------------------------------------------------
# Trash Classifier ML Project - Test script for the usage of Buttons
# Expected behaviour: the white LED should turn on for a little while as long as the button is pressed.
# 
# (c) 2020 by Jen Fox, Microsoft
# MIT License
# --------------------------------------------------------------------------

from gpiozero import Button, PWMLED
from time import sleep
button = Button(2)
white_led = PWMLED(24) 

while True:
    if button.is_pressed:
        white_led.on()
        sleep(0.3)
    else:
        white_led.off()
        sleep(0.3)