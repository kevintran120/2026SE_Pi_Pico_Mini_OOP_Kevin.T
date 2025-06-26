from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem, Controller
from time import sleep, time

red_light = Led_Light(3, False, False)
amber_light = Led_Light(5, True, False)
green_light = Led_Light(6, False, False)

p_red_light = Led_Light(19, True, False)
p_green_light = Led_Light(17, False, False)

button = Pedestrian_Button(21, False)
buzzer = Audio_Notification(27, False)

traffic = TrafficLightSubsystem(red_light, amber_light, green_light, False)
pedestrian = PedestrianSubsystem(p_red_light, p_green_light, button, buzzer, False)
system = Controller(p_red_light, p_green_light, red_light, amber_light, green_light, button, buzzer, True)

def System_Driver():
    print("System test")
    print("testing idle state for 5 seconds")
    system.set_idle_state()
    sleep(5)
    print("testing change state for 5 seconds")
    system.set_change_state()
    sleep(5)
    print("testing walk state for 5 seconds")
    j = 50
    while j >= 0:
        system.set_walk_state()
        j -= 1
        sleep(0.1)
    sleep(5)
    print("testing warning state for a bit idk how long")
    system.set_warning_state()
    sleep(5)
    print("testing error state for a bit")
    system.error_state()
    sleep(5)

System_Driver()