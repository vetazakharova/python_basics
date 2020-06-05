from abc import ABC, abstractmethod

class Fabric(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass

class Coat(Fabric):
    @property
    def consumption(self):
        return f"The amount of fabric for the coat is {round(self.param / 6.5) + 0.5}"

class Suit(Fabric):
    @property
    def consumption(self):
        return f"The amount of fabric for the suit is {round(self.param * 2) + 0.3}"

coat = Coat(40)
suit = Suit(50)
print(coat.consumption)
print(suit.consumption)
