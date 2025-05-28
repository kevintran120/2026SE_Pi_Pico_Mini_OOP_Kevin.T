from machine import Pin, ADC
from time import sleep

# wait for usb to be ready
sleep(0.1)

# store pins
led_pin = 25
led2_pin = 20
data_pin = 13
analog_data_pin = 26

# configure pins
led = Pin(led_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)

# configure data pin
data = Pin(data_pin, Pin.IN)

# configure analog pin
adc_value = ADC(Pin(analog_data_pin))

while True:
    if data.value() == 1:
        led.value(True)
        led2.value(False)
    else:
        led.value(False)
        led2.value(True)
    print(f"Analog: {adc_value.read_u16()}")
    sleep(0.1)