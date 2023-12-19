# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import board
import neopixel
import curses
import time
from basic_colors import Blue, Green, Red
from onebyone import OneByOne
from randompixels import RandomPixels
from wavelights import WaveLights
NUM_PIXELS = 500

RIGHT_ARROW = 261
LEFT_ARROW = 260
ORDER = neopixel.RGB
pixel_pin = board.D18
pixels = neopixel.NeoPixel(
        pixel_pin, NUM_PIXELS, brightness=1, auto_write=False, pixel_order=ORDER
    )
# Simple test for NeoPixels on Raspberry Pi
light_show_index = 0
light_shows = [
    WaveLights(),
    RandomPixels(),
    OneByOne()
    ,Red()
    ,Blue()
    ,Green()
]
current_light_show = light_shows[light_show_index]
cont = True

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)
screen.nodelay(True)   

def on_char(char):
    global current_light_show
    global light_show_index
    if char == RIGHT_ARROW:
        if light_show_index + 1 >= len(light_shows):
            light_show_index = 0
        else:
            light_show_index = light_show_index + 1
        current_light_show = light_shows[light_show_index]
        print(f"Running {current_light_show.name}")
    if char == LEFT_ARROW:
        if light_show_index == 0:
            light_show_index = len(light_shows) - 1
        else:
            light_show_index = light_show_index - 1
        current_light_show = light_shows[light_show_index]
        print(f"Running {current_light_show.name}")
        

print(f"Running {current_light_show.name}")
while cont:
    char = screen.getch()
    if char > 0:
        on_char(char)
    current_light_show.tick(pixels, NUM_PIXELS)
    pixels.show()
    time.sleep(current_light_show.tick_interval)


