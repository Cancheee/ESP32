from machine import Pin, SoftI2C
from Library.HC1SR04 import HCSR04
from Library.ssd1306 import SSD1306_I2C
from time import sleep

SENSOR = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=25000)
I2C = SoftI2C(scl=Pin(17), sda=Pin(16))
OLED = SSD1306_I2C(128, 64, I2C)


while True:
    OLED.fill(0)
    distance=SENSOR.distance_cm()
    OLED.text('Distance:'+str(distance)+'cm',0,0)
    OLED.show()
    print('Distance:', distance, 'cm')
    sleep(0.1)



