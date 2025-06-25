from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep
import random

button = Pedestrian_Button(22, False)
buzzer = Audio_Notification(27, False)

freq = 100
while True:
    if button.value():
        freq += 100
        buzzer.beep(freq=freq, duration=150)
    else:
        if freq > 150:
            freq -= 5
    print(freq)