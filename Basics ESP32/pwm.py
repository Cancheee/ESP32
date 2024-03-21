from machine import Pin, PWM
from time import sleep

freq = 5000
LED = PWM(Pin(5),freq)

while True:
    for duty_cycle in range (0, 1024):
        LED.duty(duty_cycle)
        print(duty_cycle)
        sleep(0.01)