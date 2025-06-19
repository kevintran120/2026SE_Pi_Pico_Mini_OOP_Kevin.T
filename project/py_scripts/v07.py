from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem
from time import sleep, time

red_light = Led_Light(3, True)
amber_light = Led_Light(5, True)
green_light = Led_Light(7, True)

p_red_light = Led_Light(19, True)
p_green_light = Led_Light(17, True)

button = Pedestrian_Button(21, True)
buzzer = Audio_Notification(27, True)

traffic = TrafficLightSubsystem(red_light, amber_light, green_light, True)
pedestrian = PedestrianSubsystem(p_red_light, p_green_light, button, buzzer, True)