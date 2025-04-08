# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import board
import neopixel
import curses
import colors
import time
from fill import FillColor
from onebyone import OneByOne
from rainbow import Rainbow
from randompixels import RandomPixels
from single import Single
from wavelights import WaveLights
from board_group import BoardGroup
from ziggy import Ziggy

RIGHT_ARROW = 261
LEFT_ARROW = 260
ORDER = neopixel.RGB


strand1 = 200
strand2 = 200
dead_zone = 50
pixels = BoardGroup(dead_zone=dead_zone)
pixels.add_board(neopixel.NeoPixel(
    board.D18, strand1+dead_zone, brightness=1, auto_write=False, pixel_order=ORDER
), board_size=strand1 )
pixels.add_board(neopixel.NeoPixel(
    board.D21, strand2, brightness=1, auto_write=False, pixel_order=ORDER
), board_size=strand2 )


# Simple test for NeoPixels on Raspberry Pi
light_show_index = 0
light_shows = [
    Single(150)
    ,Rainbow()
    ,Ziggy()
    ,WaveLights()
    ,RandomPixels()
    ,OneByOne()
    ,FillColor(colors.RED2, "Red")
    ,FillColor(colors.ORANGE, "ORANGE")
    ,FillColor(colors.YELLOW1, "YELLOW1")
    ,FillColor(colors.GREEN, "GREEN")
    ,FillColor(colors.BLUE, "BLUE")
    ,FillColor(colors.INDIGO, "INDIGO")
    ,FillColor(colors.VIOLET, "VIOLET")
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
    current_light_show.tick(pixels, pixels.num_pixels)
    pixels.show()
    if current_light_show.tick_interval:
        time.sleep(current_light_show.tick_interval)


