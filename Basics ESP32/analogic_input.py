from machine import Pin, ADC
from time import sleep

POT = ADC(Pin(34))

POT.atten(ADC.ATTN_11DB)    # Range 0 to 3.3V 
# ADC.ATTN_0DB — the full range voltage: 1.2V
# ADC.ATTN_2_5DB — the full range voltage: 1.5V
# ADC.ATTN_6DB — the full range voltage: 2.0V
# ADC.ATTN_11DB — the full range voltage: 3.3V

POT.width(ADC.WIDTH_12BIT)  # Number of bits of ADC
# ADC.WIDTH_9BIT: range 0 to 511
# ADC.WIDTH_10BIT: range 0 to 1023
# ADC.WIDTH_11BIT: range 0 to 2047
# ADC.WIDTH_12BIT: range 0 to 4095

while True:
    value = POT.read()
    voltage = (3.3/4094)*value
    print(voltage)
    sleep(0.1)
