from abc import ABC, abstractmethod


class AbstractArmyFactory(ABC):
    @abstractmethod
    def create_unit(self): pass

    @abstractmethod
    def create_commander(self, name): pass
