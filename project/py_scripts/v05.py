from pedestrian_button import Pedestrian_button
from time import sleep

button = Pedestrian_button(22, False)

while True:
    if button.button_state:
        print("waiting")
        button.button_state = False
    sleep(0.5)