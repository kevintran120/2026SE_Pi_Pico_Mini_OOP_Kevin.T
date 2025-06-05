'''
abstraction as simple interface hides the complex
implementation of 'led light' class in 'led_light.py"
extend the implementation to provide on for duration
and flash for duration methods
'''

from led_light import Led_Light
from time import sleep

red_light = Led_Light(25, True, True)

while True:
    red_light.toggle()
    sleep(0.5)