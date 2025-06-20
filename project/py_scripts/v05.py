from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep
import random

button = Pedestrian_Button(22, False)
buzzer = Audio_Notification(27, False)

j = 100
while True:
    freq = random.randrange(j, 22000)
    if button.value():
        buzzer.beep(freq=freq, duration=100)
        j += 100
        print(j)
    else:
        buzzer.duty_u16(0)
    sleep(0.01)