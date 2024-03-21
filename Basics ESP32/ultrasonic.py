from machine import Pin
from Library.HC1SR04 import HCSR04
from time import sleep
# HC-SR04
# VCC       ->  5V
# TRIGGER   ->  
# ECHO      ->  
# GND       ->  

SENSOR = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=25000)

while True:
    distance=SENSOR.distance_cm()
    print('Distance:', distance, 'cm')
    sleep(0.1)



