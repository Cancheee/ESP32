from machine import Pin, SoftI2C
from Library.ssd1306 import SSD1306_I2C

# REF
#https://docs.micropython.org/en/latest/library/machine.I2C.html

# VCC (3.3V)
# SCL (System Clock)
# SDA (System Data)
I2C = SoftI2C(scl=Pin(5), sda=Pin(4))
OLED = SSD1306_I2C(128, 64, I2C)
OLED.text('Hello',0,0)
OLED.text('World!',0,20)
OLED.text('from Guatemala!',0,40)
OLED.show()