from machine import Pin
from time import sleep

BUTTON_1 = Pin(2,Pin.IN)
BUTTON_2 = Pin(4,Pin.IN)

#7 Segment
LED_1= Pin(33,Pin.OUT)      #A
LED_2 = Pin(25,Pin.OUT)     #B
LED_3 = Pin(26,Pin.OUT)     #C
LED_4 = Pin(27,Pin.OUT)     #D
LED_5 = Pin(14,Pin.OUT)     #E
LED_6 = Pin(12,Pin.OUT)     #G

while True:
    if (BUTTON_1.value()==True and BUTTON_2.value()==False):
        LED_1.value(True)
        LED_2.value(False)
        LED_3.value(False)
        LED_4.value(True)
        LED_5.value(True)
        LED_6.value(True)

    elif (BUTTON_1.value()==True and BUTTON_2.value()==True):
        LED_1.value(False)
        LED_2.value(False)
        LED_3.value(True)
        LED_4.value(False)
        LED_5.value(False)
        LED_6.value(False)

    elif (BUTTON_1.value()==False and BUTTON_2.value()==True):
        LED_1.value(False)
        LED_2.value(False)
        LED_3.value(False)
        LED_4.value(False)
        LED_5.value(True)
        LED_6.value(False)
        
    else: 
        LED_1.value(True)
        LED_2.value(True)
        LED_3.value(True)
        LED_4.value(True)
        LED_5.value(True)
        LED_6.value(True)

    sleep(0.1)