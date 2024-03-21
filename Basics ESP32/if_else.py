from machine import Pin
from time import sleep

BUTTON = Pin(4,Pin.IN)
LED_GREEN = Pin(5,Pin.OUT)
LED_RED = Pin(18,Pin.OUT)

while True:
    if BUTTON.value()==True:
        LED_GREEN.value(True)
        LED_RED.value(False)
    else:
        LED_GREEN.value(False)
        LED_RED.value(True)

