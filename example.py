from machine import Pin, SPI, I2C, SoftI2C
from vl53l0x_ada import VL53L0X
import time

vl_i2c = I2C(1,sda=Pin(14),scl=Pin(15))

print("i2c scan:",vl_i2c.scan())

vl = VL53L0X(vl_i2c)

x = 0
while True:
    vl.start_range_request()
    if vl.reading_available():
        print("Distance ==>  ",vl.get_range_value())
    else:
        # Do something else as long as no reading is
        # available
        x += 1
        print("Waiting for reading",x)
    time.sleep(0.03)
