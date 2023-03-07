# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""Example for Pico. Blinks the built-in LED."""
import time
import board
import digitalio

led_1 = digitalio.DigitalInOut(board.GP13)
led_1.direction = digitalio.Direction.OUTPUT

led_2 = digitalio.DigitalInOut(board.GP12)
led_2.direction = digitalio.Direction.OUTPUT

led_3 = digitalio.DigitalInOut(board.GP11)
led_3.direction = digitalio.Direction.OUTPUT

while True:
    led_1.value = True
    led_2.value = False
    led_3.value = False
    time.sleep(0.5)

    led_1.value = False
    led_2.value = True
    led_3.value = False
    time.sleep(0.5)

    led_1.value = False
    led_2.value = False
    led_3.value = True
    time.sleep(0.5)
    
    led_1.value = True
    led_2.value = True
    led_3.value = False
    time.sleep(0.5)

    led_1.value = False
    led_2.value = True
    led_3.value = True
    time.sleep(0.5)

    led_1.value = True
    led_2.value = True
    led_3.value = True
    time.sleep(0.5)

