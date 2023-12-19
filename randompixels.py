from base import LightBase
import random
import colors
COLOR_CHOICES =[
    colors.RED1,
 colors.BLUE,
 colors.GREEN,
 colors.BLACK,
 colors.PINK,
 colors.AZURE4,
 colors.MAGENTA,
 colors.LIMEGREEN,
 colors.MIDNIGHTBLUE]
class RandomPixels(LightBase):
    def __init__(self) -> None:
        self.len = len(COLOR_CHOICES) - 1
        
    @property
    def name(self):
        "Random"
    
    @property
    def tick_interval(self):
        return 0.01

    def tick(self, pixels, max):
        for p in range(0, max):
            pixels[p] = COLOR_CHOICES[random.randint(0,self.len)]
        
        