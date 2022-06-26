# ------------------------------------------------------------------------
# Trash Classifier ML Project - Test script for the usage of LEDs
# Expected behaviour: switches all available LEDs on and off for 1 second.
# 
# (c) 2020 by Jen Fox, Microsoft
# MIT License
# --------------------------------------------------------------------------

from gpiozero import LED
from time import sleep

# Declare leds
yellow_led = LED(17)
blue_led = LED(27)
green_led = LED(22)
red_led = LED(23)
white_led = LED(24)

# Create a dict with "LED ID" -> LED object
available_leds = {
    "yellow" : yellow_led,
    "blue" : blue_led,
    "green" : green_led,
    "red" : red_led,
    "white" : white_led
}

# Keeps the led {@code led} on for 1s before turning off again
# @param led Object LED
def blink_led(led):
    led.on()
    sleep(1)
    led.off()
    sleep(1)

# Main function
while 1:
    for led_color, led_object in available_leds.items():
        print("Blinking %s LED" % led_color)
        blink_led(led_object)