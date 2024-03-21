from machine import Pin, ADC
from time import sleep

X_1 = ADC(Pin(35))
Y_1 = ADC(Pin(34))

X_1.atten(ADC.ATTN_11DB)    # Range 0 to 3.3V 
Y_1.atten(ADC.ATTN_11DB)    # Range 0 to 3.3V 

BUTTON = Pin(18, Pin.IN)

while True:
    axis_x = X_1.read()
    axis_y = Y_1.read()

    state = BUTTON.value()
    print('ejeX: ', axis_x)
    print('ejeY: ', axis_y)
    print('Button: ', state)

    if axis_x < 2048:
        print("Derecha")
    elif axis_x > 2048:
        print("Izquierda")
    elif axis_y > 2048:
        print("Arriba")
    elif axis_y < 2048:
        print("Abajo")
    sleep(0.1)