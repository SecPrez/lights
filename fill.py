import colors
from base import LightBase


class FillColor(LightBase):
    
    def __init__(self, color, name) -> None:
        self.color = color
        self.color_name = name
    @property
    def name(self):
        return self.color_name
    
    @property
    def tick_interval(self):
        return 1

    def tick(self, pixels, max):
        pixels.fill(self.color)
        
