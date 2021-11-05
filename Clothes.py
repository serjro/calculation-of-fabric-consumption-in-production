from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self,VH):
        self.VH=VH
    @property
    @abstractmethod
    def calculation(self):
        pass

    def __add__(self, other):
        return self.calculation+other.calculation

class Coat(Clothes):
    @property
    def calculation(self):
        return self.VH/6.5+0.5

class Suit(Clothes):
    @property
    def calculation(self):
        return 2*self.VH+0.3

coat1=Coat(10)
suit1=Suit(10)
print(f"Потребляемый обьем ткани - {coat1+suit1}")
