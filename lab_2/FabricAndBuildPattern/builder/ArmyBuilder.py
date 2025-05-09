from lab_2.FabricAndBuildPattern.base.AbstractArmyFactory import AbstractArmyFactory
from lab_2.FabricAndBuildPattern.commanders.Commander import Commander


class ArmyBuilder:
    def __init__(self, factory: AbstractArmyFactory, commander_name: str):
        self._army = factory
        self._commander = factory.create_commander(commander_name)

    def add_units(self, count: int) -> None:
        for i in range(count):
            unit = self._army.create_unit()
            self._commander.add_unit(unit)
        return self

    def build(self) -> Commander:
        return self._commander
