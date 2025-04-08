# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
from board_group import BoardGroup

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 50

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB
group = BoardGroup(num_pixels)
pixels = neopixel.NeoPixel(
    board.D18, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
pixels2 = neopixel.NeoPixel(
    board.D21, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
group.add_board(pixels)
group.add_board(pixels2)
group.fill((255, 0, 0))
group.show()
group[0] = (0,255,255)
group.show()