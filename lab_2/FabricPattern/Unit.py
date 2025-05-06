from abc import ABC, abstractmethod


class Unit(ABC):
    @abstractmethod
    def attack(self): ...

    @abstractmethod
    def defend(self): ...

    @abstractmethod
    def move(self): ...
