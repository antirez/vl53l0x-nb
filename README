This code is a modified version of the Adafruit VL53L0X sensor distance driver.
I found a modified version by Kevin Zhu that converted the code from CircuitPython to MicroPython. Then I added support for the much needed non-blocking reading mode.

In blocking mode, the reading is performed like this:

    vl_i2c = I2C(1,sda=Pin(14),scl=Pin(15))
    vl = VL53L0X(vl_i2c)
    vl.range

The call to `vl.range` is blocking (in general defining what is a function as a property is bad, but if the latency is high, the property shell is even more misleading). Because the sensor phisically requires tens of milliseconds in order to finish the measure.

The driver does not support an interrupt mode with the callback AFAIK, so I
modified it in order to have two halves to perform the measurement: one that
starts the range process and the other that reads the result when available:

    vl.start_range_request()
    if vl.reading_available():
        print(vl.get_range_value())

You can check if the request is already in progress with `vl.range_started`, which is set to True if a measurement process is already happening.

So a typical loop will look like:

    while True:
        if vl.range_started == False: vl.start_range_request()
        if vl.reading_available():
            ... do something with vl.get_range_value() ...

If a request was not initiated, `get_range_value()` just returns None.

In order to avoid confusion with the many forks of this code, I called the file vl53l0x_nb.py ("nb" = non blocking).

The driver is not clearly written and I don't want to make a rewrite because of the absurd ST(trademark) policy of not providing documentation for the chip, but if you have improvements, please send a pull request. Thanks.
