*********
pi-bme280
*********
The pi-bme280 package is a Python 3 library used to communicate and control the BOSCH BME280 combined humidity and
pressure sensor. sensors. It was designed to be used primarily with the Raspberry Pi and depends on the `RPi.GPIO`_ library.

The BME280 is as combined digital humidity, pressure and temperature sensor based on
proven sensing principles. The sensor module is housed in an extremely compact metal-lid LGA
package with a footprint of only 2.5 × 2.5 mm2 with a height of 0.93 mm. Its small dimensions
and its low power consumption allow the implementation in battery driven devices such as
handsets, GPS modules or watches. The BME280 is register and performance compatible to
the Bosch Sensortec BMP280 digital pressure sensor (see chapter 5.2 for details).

The BME280 achieves high performance in all applications requiring humidity and pressure
measurement. These emerging applications of home automation control, in-door navigation,
health care as well as GPS refinement require a high accuracy and a low TCO at the same
time.

The humidity sensor provides an extremely fast response time for fast context awareness
applications and high overall accuracy over a wide temperature range.

The pressure sensor is an absolute barometric pressure sensor with extremely high accuracy
and resolution and drastically lower noise than the Bosch Sensortec BMP180.

The integrated temperature sensor has been optimized for lowest noise and highest resolution.
Its output is used for temperature compensation of the pressure and humidity sensors and can
also be used for estimation of the ambient temperature.

The sensor provides both SPI and I2C interfaces and can be supplied using 1.71 to 3.6 V for the
sensor supply V DD and 1.2 to 3.6 V for the interface supply V DDIO . Measurements can be
triggered by the host or performed in regular intervals. When the sensor is disabled, current
consumption drops to 0.1 μA.

The package was tested using the `Raspberry Pi 3 - Model B` with the following software:
* Raspbian GNU/Linux 8.0 (jessie)
* Linux kernel 4.4.31-v7+ #921
* RPi.GPIO 0.6.3
* Python 3.4.2

If you run into any problems, please let me know or create an `issue`_ on the GitHub project page:

::

    https://github.com/drohm/pi-sht1x

The data sheet for the BME280 series of sensors can be found here:

::

    http://bit.ly/2evWjCm

This library provides the following functionality:


* Taking temperature measurements
* Taking humidity measurements
* Make dew point calculations
* Change the supplied voltage (5V, 4V, 3.5V, 3V, 2.5V)
* Enable or disable CRC checking
* Reading the Status Register
* Writing to the Status Register, provides the following functionality:
* Turn ``otp_no_reload`` on (will save about 10ms per measurement)
* Turn on the internal heater element (for functionality analysis, refer to the data sheet list above for more information)
* Change the resolution of measurements, High (14-bit temperature and 12-bit humidity) or Low (12-bit temperature and 8-bit humidity)


Installation
============
Installation is pretty simple:

::

    pip3 install pi-sht1x

Note that to install packages into the system-wide PATH and site-packages, elevated privileges are often required (sudo). You can try using ``install -user`` or `virtualenv`_ to do unprivileged installs.


Usage
=====
When instantiating a SHT1x object, the following default values are used if not specified:

::

    gpio_mode:        GPIO.BOARD
    vdd:              3.5V
    resolution:       High (14-bit temperature & 12-bit humidity)
    heater:           False
    otp_no_reload:    False
    crc_check:        True

Command Line - REPL
-------------------
You can invoke the SHT1x class directly from the REPL. In order to use the library you need to import the package:

::

    from pi_sht1x import SHT1x

Now you can create the sensor object and take measurements:

::

    with SHT1x(18, 23, gpio_mode=GPIO.BCM) as sensor:
        temp = sensor.read_temperature()
        humidity = sensor.read_humidity(temp)
        sensor.calculate_dew_point(temp, humidity)
        print(sensor)

This will create the SHT1x object using ``data_pin=18``, ``sck_pin=23``, ``gpio_mode=GPIO.BCM``, and default values for ``vdd`` (3.5V), ``resolution`` (High), ``heater`` (False), ``otp_no_reload`` (False), and ``crc_check`` (True). The output will look something like this:

::

    Temperature: 24.05*C [75.25*F]
    Humidity: 22.80%
    Dew Point: 1.38*C

Note that this library should be used with a context manager like the ``with`` statement. Using it with a context manager will allow the program to properly clean up after itself and reset the GPIO pins back to default states.

examples.py
-----------
This script, located in the examples folder, includes several ways to use the SHT1x class to take temperature, humidity, and dew point measurements. In order to use the script, be sure to update the ``DATA_PIN`` and ``SCK_PIN`` constants near the top of the file with the pin numbers you're using locally in your setup:

::

    DATA_PIN = 18
    SCK_PIN = 23

Based on the fact that the data sheet recommends 3.3V to power the sensor, the default voltage, if not specified when instantiating the object, is 3.5V. If you're using 5V to power the sensor, be sure to set that value when creating the object. To run the script:

::

    sudo python3 examples/examples.py

Running the script exercises all of the functionality for the sensor. Be sure to look through the script to see what you can do and how to customize using the sensor. Sample output:

::

    $ sudo python3 examples/examples.py
    Test: using default values: 3.5V, High resolution, no heater, otp_no_reload off, CRC checking enabled...
    Temperature: 24.49*C [76.04*F]
    Humidity: 20.68%
    Dew Point: 0.47*C
    
    Temperature: 24.48*C [76.02*F]
    Humidity: 20.68%
    Dew Point: 0.46*C
    
    Temperature: 24.47*C [76.01*F]
    Humidity: 20.68%
    Dew Point: 0.45*C
    
    Temperature: 24.51*C [76.06*F]
    Humidity: 20.68%
    Dew Point: 0.47*C
    
    Temperature: 24.51*C [76.06*F]
    Humidity: 20.68%
    Dew Point: 0.47*C
    Test complete.
    
    Test: reading all measurements using GPIO.BCM mode, 3V, High resolution, heater off, otp_no_reload off, and CRC check on.
    Temperature: 24.48*C [76.02*F]
    Humidity: 20.61%
    Dew Point: 0.42*C
    
    Temperature: 24.46*C [75.98*F]
    Humidity: 20.61%
    Dew Point: 0.40*C
    
    Temperature: 24.46*C [75.98*F]
    Humidity: 20.61%
    Dew Point: 0.40*C
    
    Temperature: 24.48*C [76.02*F]
    Humidity: 20.68%
    Dew Point: 0.46*C
    
    Temperature: 24.48*C [76.02*F]
    Humidity: 20.65%
    Dew Point: 0.44*C
    Test complete.
    .
    .
    .

The `RPi.GPIO`_ module requires root privileges in order to communicate with the GPIO pins on the Raspberry Pi so you need to run your scripts as root (sudo).

sensor.py
---------
This script is callable from the terminal and the sensor parameters are passed into the script.

::

    sudo python3 sensor.py 18 23 -g 'BCM'

This executes the sensor script using ``data_pin=18``, ``sck_pin=23``, and ``gpio_mode=GPIO.BCM``. The script will then create an instance of the SHT1x class and read in the temperature, humidity, and calculate the dew point five times, sleeping 2 seconds in between each measurement. The output will looks something like this:

::

    $ sudo python3 examples/sensor.py 18 23 -g 'BCM'
    Temperature: 24.05*C [75.25*F]
    Humidity: 22.79%
    Dew Point: 1.37*C
    
    Temperature: 24.03*C [75.21*F]
    Humidity: 22.79%
    Dew Point: 1.36*C
    
    Temperature: 24.01*C [75.16*F]
    Humidity: 22.79%
    Dew Point: 1.33*C
    
    Temperature: 24.01*C [75.17*F]
    Humidity: 22.86%
    Dew Point: 1.38*C
    
    Temperature: 24.02*C [75.19*F]
    Humidity: 22.86%
    Dew Point: 1.39*C

To get a listing of all the parameters you can provide to the script, use `python3 sensor.py -h` for help:

::

    $ sudo python3 examples/sensor.py -h
    usage: sensor.py [-h] [-g {BCM,BOARD}] [-v {5V,4V,3.5V,3V,2.5V}]
                     [-r {HIGH,LOW}] [-e] [-o] [-c]
                     data-pin sck-pin
    
    Reads the temperature and relative humidity from the SHT1x series of sensors
    using the pi_sht1x library.
    
    positional arguments:
      data-pin              Data pin used to connect to the sensor.
      sck-pin               SCK pin used to connect to the sensor.
    
    optional arguments:
      -h, --help            show this help message and exit
      -g {BCM,BOARD}, --gpio-mode {BCM,BOARD}
                            RPi.GPIO mode used, either GPIO.BOARD or GPIO.BCM.
                            Defaults to GPIO.BCM.
      -v {5V,4V,3.5V,3V,2.5V}, --vdd {5V,4V,3.5V,3V,2.5V}
                            Voltage used to power the sensor. Defaults to 3.5V.
      -r {HIGH,LOW}, --resolution {HIGH,LOW}
                            Resolution used by the sensor, 14/12-bit or 12-8-bit.
                            Defaults to High.
      -e, --heater          Used to turn the internal heater on (used for
                            calibration).
      -o, --otp-no-reload   Used to enable OTP no reload, will save about 10ms per
                            measurement.
      -c, --no-crc-check    Performs CRC checking.


Credits
=======
This module was done for fun and to learn how to communicate with serial devices using Python and the Raspberry Pi. I referred to the following projects from time to time when I hit a stumbling block (there were many...):

* `Jonathan Oxer`_ 
* `Luca Nobili`_ 

.. _RPi.GPIO: http://pypi.python.org/pypi/RPi.GPIO
.. _Raspberry Pi 3 - Model B: https://www.adafruit.com/products/3055
.. _issue: https://github.com/drohm/pi-bme280/issues
.. _virtualenv: https://pypi.python.org/pypi/virtualenv
.. _Jonathan Oxer: https://github.com/practicalarduino/SHT1x
.. _Luca Nobili: https://bitbucket.org/lunobili/rpisht1x
