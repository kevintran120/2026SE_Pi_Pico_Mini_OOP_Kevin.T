from audio_notification import Audio_Notification
from pedestrian_button import Pedestrian_button
from time import sleep

buzzer = Audio_Notification(27, True)
button = Pedestrian_button(22, False)

while True:
    if button.button_state:
        buzzer.warning_on()
        button.button_state = False
    sleep(0.5)
    buzzer.warning_off()