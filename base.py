from abc import ABC, abstractmethod

class LightBase(ABC):
    @property
    @abstractmethod
    def tick_interval(self):
        pass
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod    
    def tick(self, pixels, max):
        pass
