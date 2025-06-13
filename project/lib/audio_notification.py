from machine import Pin, PWM
from time import sleep, time

class Audio_Notification(PWM):
    def __init__(self, pin, debug=False):
        super().__init__(Pin(pin))
        self.__pin = pin
        self.__debug = debug
        self.duty_u16(0) # start with buzzer off
        self.__last_toggle_time = time()
    
    def beep(self, freq=1000, duration=500):
        if self.__debug:
            print("Beep")
        self.freq(freq)
        self.duty_u16(32768) # 50% duty cycle
        sleep(duration / 1000)
        self.duty_u16(0) # turn off after sleep

    def warning_on(self):
        if self.__debug:
            print("Warning on")
        now = time()
        if now - self.__last_toggle_time >= 0.5:
            self.beep(freq=500, duration=100)
            self.__last_toggle_time = now

    def warning_off(self):
        if self.__debug:
            print("Warning off")
        self.duty_u16(0) # turn off sound