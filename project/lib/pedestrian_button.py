from machine import Pin
from time import ticks_ms, ticks_diff

class Pedestrian_Button(Pin):
    """
    a class that gives a button pedestrian button functionality with a timer
    also adds functionality that sees if theres someone waiting at the light

    arguments:
        pin (int): GPIO pin number for the button

    examples:
        button = Pedestrian_Button(22) # button connected to pin 22
        button.
    """
    # child class inherits the parent 'pin' class
    def __init__(self, pin, debug):
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = 0 # tracks the last time the button was pressed
        self.__pedestrian_waiting = False
        self.irq(trigger=Pin.IRQ_RISING, handler=self.callback)
        
    def button_state(self, value=None):
        if value is None:
            # getter
            if self.__debug:
                print(f"Button connected to Pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}")
            return self.__pedestrian_waiting
        else:
            self.__pedestrian_waiting = bool(value) # convert to bool to ensure proper value type
            if self.__debug:
                print(f"Button state on pin {self.__pin} set to {self.__pedestrian_waiting}")
    
    def callback(self, pin):
        """
        changes the button's state when it is pressed
        also has debounce logic (so you cant double click)
        """
        current_time = ticks_ms() # get the current time in ms
        if (ticks_diff(current_time, self.__last_pressed) > 200): # 200ms debounce delay
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")