from led_light import Led_Light
from time import sleep

# normal light
light = Led_Light(3, False, False)
# debug light
debug_light = Led_Light(5, False, True)
# flashing light
flashing_light = Led_Light(6, True, False)

print("testing on() on normal light")
light.on()
sleep(1)

print("testing off() on normal light")
light.off()
sleep(1)

print("testing toggle() and debug messages")
debug_light.toggle()
sleep(1)
debug_light.toggle()
sleep(1)

# should do a test for the led light state

print("testing flash on flashing light")
while True:
    flashing_light.flash()