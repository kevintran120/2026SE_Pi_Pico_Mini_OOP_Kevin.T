from pedestrian_button import Pedestrian_button
from time import sleep

button = Pedestrian_button(22, False)

while True:
    print(button.button_state())
    sleep(0.5)
    