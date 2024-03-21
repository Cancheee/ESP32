from machine import Pin
from time import sleep

# PinOut
LED = Pin(2, Pin.OUT)
BUTTON = Pin(14, Pin.IN)

# Loop 1
# while True:
#     LED.value(BUTTON.value())
#     # sleep(0.1)

# Loop 2
while True:
    LED.value(True)
    sleep(2)
    LED.value(False)
    sleep(2)
