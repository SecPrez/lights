from base import LightBase
import colors

class Rainbow(LightBase):
    def __init__(self) -> None:
        self.indexes = {}
        self.directions = {}
      
    @property
    def name(self):
        return "Rainbow"
    
    @property
    def tick_interval(self):
        return 0

    def tick(self, pixels, max):
        pixels.fill((0, 0, 0))
        
        for x in range(0,10):
            pixels[self.get_index(x, max)] = colors.RED1
        for x in range(10,20):
            pixels[self.get_index(x, max)] = colors.ORANGE
        for x in range(20,30):
            pixels[self.get_index(x, max)] = colors.YELLOW1
        for x in range(30,40):
            pixels[self.get_index(x, max)] = colors.GREEN
        for x in range(40,50):
            pixels[self.get_index(x, max)] = colors.BLUE
        for x in range(50,60):
            pixels[self.get_index(x, max)] = colors.INDIGO
        for x in range(60,70):
            pixels[self.get_index(x, max)] = colors.VIOLET
        
       

    def get_index(self, inital_offset, max):
        index = self.indexes.get(inital_offset, inital_offset)
        direction = self.directions.get(inital_offset, True)
        if index + 1 == max: 
            self.directions[inital_offset] = False
            direction = False
        if not direction and index == 0:
            self.directions[inital_offset] = True
            direction = True
        if direction:
            self.indexes[inital_offset] = index + 1
        if not direction:
            self.indexes[inital_offset] = index - 1
        return index
        
        