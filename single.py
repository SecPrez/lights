from base import LightBase
import colors

class Single(LightBase):
    def __init__(self, index) -> None:
        self.index = index
      
      
    @property
    def name(self):
        return "Single"
    
    @property
    def tick_interval(self):
        return 0

    def tick(self, pixels, max):
        pixels.fill((0, 0, 0))
        pixels[self.index] = colors.RED1
        
        
       

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
        
        