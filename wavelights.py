from base import LightBase
import random
import colors

COLOR_CHOICES = [
    colors.RED1,
    # colors.RED1,
    # colors.RED1,
    colors.WHITE,
    # colors.WHITE,
    # colors.WHITE,
    colors.BLUE,
    # colors.BLUE,
    # colors.BLUE,
    
    #  colors.PINK,
    #  colors.AZURE4,
    #  colors.MAGENTA,
    #  colors.LIMEGREEN,
    #  colors.MIDNIGHTBLUE
]
COLOR_CHOICES.extend(colors.BLACK * 5)
class WaveLights(LightBase):
    def __init__(self) -> None:
        self.len = len(COLOR_CHOICES) - 1
        self.start = 0

    @property
    def name(self):
        "Wave"

    @property
    def tick_interval(self):
        return .5

    def tick(self, pixels, max):
        c = self.start
        for x in range(0, max):
            pixels[x] = COLOR_CHOICES[c]
            c = (c + 1) % self.len
        self.start = (self.start + 1) % self.len
