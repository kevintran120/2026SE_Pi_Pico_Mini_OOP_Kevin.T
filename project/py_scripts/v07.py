from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem
from time import sleep, time

red_light = Led_Light(3, False, False)
amber_light = Led_Light(5, False, False)
green_light = Led_Light(6, False, False)

p_red_light = Led_Light(19, False, True)
p_green_light = Led_Light(17, False, True)

button = Pedestrian_Button(21, True)
buzzer = Audio_Notification(27, True)

traffic = TrafficLightSubsystem(red_light, amber_light, green_light, True)
pedestrian = PedestrianSubsystem(p_red_light, p_green_light, button, buzzer, True)

def Traffic_Subsystem_Driver():
    # print("testing traffic light in 5 seconds")
    # sleep(5)
    # print("testing red")
    # traffic.show_red()
    # print("pass if red on, amber and green off")
    # sleep(5)
    # print("testing amber")
    # traffic.show_amber()
    # print("pass if amber on, red and green off")
    # sleep(5)
    # print("testing green")
    # traffic.show_green()
    # print("pass if green on, red and amber off")

    while True:
        traffic.show_red()
        sleep(0.1)
        traffic.show_amber()
        sleep(0.1)
        traffic.show_green()
        sleep(0.1)

Traffic_Subsystem_Driver()