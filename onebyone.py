from base import LightBase
import colors

class OneByOne(LightBase):
    def __init__(self) -> None:
        self.indexes = {}
        self.directions = {}
      
    @property
    def name(self):
        "OneByOne"
    
    @property
    def tick_interval(self):
        return 0.0000

    def tick(self, pixels, max):
        pixels.fill((0, 0, 0))
        
        for x in range(0,10):
            pixels[self.get_index(x, max)] = colors.BLUE
        for x in range(10,20):
            pixels[self.get_index(x, max)] = colors.WHITE
        
        for x in range(20,30):
            pixels[self.get_index(x, max)] = colors.RED1
        
       

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
        
        