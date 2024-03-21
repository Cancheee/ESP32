from machine import Pin
from time import sleep

LED_1 = Pin(12, Pin.OUT)
LED_2 = Pin(14, Pin.OUT)
LED_3 = Pin(27, Pin.OUT)

def Sequence(State1, State2, State3, Time):
    LED_1.value(State1)
    LED_2.value(State2)
    LED_3.value(State3)
    sleep(Time)

while True:
    Sequence(True, False, False, 1)
    Sequence(True, True, False, 1)
    Sequence(True, True, True, 1)
    Sequence(False, True, True, 1)
    Sequence(False, False, True, 1)
    Sequence(False, False, False, 1)