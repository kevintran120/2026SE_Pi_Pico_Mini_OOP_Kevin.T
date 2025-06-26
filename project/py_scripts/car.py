from pedestrian_button import Pedestrian_Button
from machine import Pin, PWM
from time import sleep

button = Pedestrian_Button(22, False)
buzzer = PWM(Pin(27))

buzzer.duty_u16(4000)
freq = 100
while True:
    if button.value():
        freq += 2
    else:
        if freq > 150:
            freq -= 25
    buzzer.freq(freq)
    print(freq)
    sleep(0.005)