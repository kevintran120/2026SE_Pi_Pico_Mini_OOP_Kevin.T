from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem, Controller
from time import sleep, time

debug = False

red_light = Led_Light(3, False, debug)
amber_light = Led_Light(5, True, debug)
green_light = Led_Light(6, False, debug)

p_red_light = Led_Light(19, True, debug)
p_green_light = Led_Light(17, False, debug)

button = Pedestrian_Button(21, debug)
buzzer = Audio_Notification(27, debug)

traffic = TrafficLightSubsystem(red_light, amber_light, green_light, debug)
pedestrian = PedestrianSubsystem(p_red_light, p_green_light, button, buzzer, debug)

controller = Controller(
    p_red_light,
    p_green_light,
    red_light,
    amber_light,
    green_light,
    button,
    buzzer,
    debug
)

while True:
    controller.update()
    sleep(0.1)