from machine import Pin
from time import sleep, time

class Led_Light(Pin):
    # child inherits pin class
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing

    def on(self):
        # method overriding polymorphism of the parent class
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is on")

    def off(self):
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is off")
        
    def toggle(self):
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
            self.off()

    @property
    def led_light_state(self):
        return self.value()
    
    @led_light_state.setter
    def led_light_state(self, value):
        if value == 1:
            self.off()
        elif value == 0:
            self.on()