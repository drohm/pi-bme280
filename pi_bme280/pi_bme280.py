"""
BME280 library
"""
import time
import math


class BME280Error(Exception):
    pass


try:
    import RPi.GPIO as GPIO
except ImportError:
    raise BME280Error('Could not import the RPi.GPIO package (http://pypi.python.org/pypi/RPi.GPIO). Exiting.')


class BME280:
    def __init__(self):
        pass


if __name__ == "__main__":
    pass
