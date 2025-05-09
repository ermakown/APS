from abc import ABC, abstractmethod


class Unit(ABC):
    @abstractmethod
    def attack(self): pass

    @abstractmethod
    def defend(self): pass

    @abstractmethod
    def move(self): pass
