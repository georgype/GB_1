from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def fabric_size(self):
        pass


class Coat(Clothes):
    @property
    def fabric_size(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):
    @property
    def fabric_size(self):
        return self.param * 2 + 0.3


my_coat = Coat(25)
my_suit = Suit(3)

print(my_coat.fabric_size)
print(my_suit.fabric_size)
print(f'Общий расход ткани {my_suit.fabric_size + my_coat.fabric_size}')
