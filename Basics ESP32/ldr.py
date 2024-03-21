from machine import Pin, ADC
from time import sleep

LDR = ADC(Pin(34))
RELE = Pin(4, Pin.OUT)
LDR.atten(ADC.ATTN_11DB)

while True: 
    lectura = LDR.read()
    print(lectura)

    if lectura>3000:
        RELE.on()
    else:
        RELE.off()
    
    sleep(0.1)