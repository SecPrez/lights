import colors
from base import LightBase


class Red(LightBase):
        
    @property
    def name(self):
        return "Red"
    
    @property
    def tick_interval(self):
        return 1

    def tick(self, pixels, max):
        pixels.fill(colors.RED1)
        

class Blue(LightBase):
        
    @property
    def name(self):
        return "Blue"
    
    @property
    def tick_interval(self):
        return 1

    def tick(self, pixels, max):
        pixels.fill((0, 255, 0))

class Green(LightBase):
        
    @property
    def name(self):
        return "Green"
    
    @property
    def tick_interval(self):
        return 1

    def tick(self, pixels, max):
        pixels.fill((0, 0, 255))