from machine import Pin
from time import sleep

LED = Pin(4, Pin.OUT)

for i in range(0,10,1):
    print(i)
    LED.on()
    sleep(1)
    LED.off()
    sleep(1)

# for i in range(0,10,1):
#     print(i)
#     LED.value(True)
#     sleep(1)
#     LED.value(False)
#     sleep(1)
