# ,pdi;es
from machine import I2C, Pin
from time import sleep

# very important ‼️‼️‼️
# this module needs to be saved in the raspberry pi pico in order for the lcd i2c to be used
from pico_i2c_lcd import I2cLcd

# creating an i2c object, specifying the data (sda) and clock (scl) pins usedi n the raspberry pi pico
# any sda and scl pins in the rasberry pi pico can be used
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# getting i2c address
I2C_ADDR = i2c.scan()[0]

# creating an lcd object using the i2c address and specifying number of rows and columns in the lcd
# lcd number of rows = 2, number of columns = 16
lcd = I2cLcd(i2c, I2C_ADDR, 1, 16)

# continuously print and clear hello world in hte lcd screen while the board has power
while True:
    # putstr method allows printing of the text in the lcd screen
    # for other methods that can be used, check Lcd_api module
    lcd.putstr("M")
    sleep(0.5)
    lcd.putstr("a")
    sleep(0.5)
    lcd.putstr("t")
    sleep(0.5)
    lcd.putstr("c")
    sleep(0.5)
    lcd.putstr("h")
    sleep(0.5)
    lcd.putstr("a")
    sleep(0.5)
    lcd.clear()