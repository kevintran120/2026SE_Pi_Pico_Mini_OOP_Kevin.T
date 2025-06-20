from audio_notification import Audio_Notification
from time import sleep

buzzer = Audio_Notification(27, True)

print("testing short and long beep")
buzzer.beep(1000, 100)
sleep(2)
print("testing short and long beep")
buzzer.beep(1000, 500)
sleep(2)

print("test warning on")
while True:
    buzzer.warning_on()