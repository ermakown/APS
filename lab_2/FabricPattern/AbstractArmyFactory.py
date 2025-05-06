from abc import ABC, abstractmethod


class AbstractArmyFactory(ABC):
    @abstractmethod
    def create_unit(self): ...

    @abstractmethod
    def create_commander(self, name): ...
