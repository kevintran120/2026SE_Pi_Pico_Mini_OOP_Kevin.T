from machine import Pin, ADC, PWM
from time import sleep

# wait for usb to be ready
sleep(0.1)

# store pins
led_pin = 25
led2_pin = 20
data_pin = 13
analog_data_pin = 26
servo_pin = 10

# configure pins
led = PWM(Pin(led_pin))
led2 = PWM(Pin(led2_pin))

# set pwm frequencies for leds
led.freq(1000)
led2.freq(1000)

servo = PWM(Pin(servo_pin))

# set servo frequency
servo.freq(50) #pulse every 20ms

# configure data pin
data = Pin(data_pin, Pin.IN)

# configure analog pin
analog_data = ADC(Pin(analog_data_pin))

#functin to calculate pulse width in microsenc
def set_angle(angle):
    # clamps input angle to 1-100
    angle = min(max(angle, 0), 180)
    return int(500 + (angle / 180) * 2000)

# fucntion to linearly map values
def map_range(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    adc_value = analog_data.read_u16() # 0-65535
    if data.value() == 1:
        led.duty_u16(adc_value)
        led2.duty_u16(adc_value)
    else:
        led.duty_u16(0)
        led2.duty_u16(0)
    mapped_value = map_range(adc_value, 0, 65535, 0, 180)
    servo.duty_ns(set_angle(mapped_value) * 1000)
    print(f"Digital: {data.value()}, Analog: {adc_value}, Servo: {servo.duty_ns()}")
    sleep(0.1)