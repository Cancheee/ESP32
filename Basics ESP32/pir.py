from machine import Pin
from time import sleep

PIR = Pin(34,Pin.IN)
BUZZER = Pin(0,Pin.OUT)
LED = Pin(2,Pin.OUT)


while True:
    print(PIR.value())
    if PIR.value()==True:
        BUZZER.on()
        LED.on()
    else:
        BUZZER.off()
        LED.off()
    sleep(0.1)

# while True:
#     print(PIR.value())
#     if PIR.value()==True:
#         BUZZER.value(True)
#         LED.value(True)
#     else:
#         BUZZER.value(False)
#         LED.value(False)
#     sleep(0.1)