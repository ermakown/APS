from AbstractArmyFactory import AbstractArmyFactory
from UnitRealizations import Infantry, Cavalry, Artillery
from ArmyCommanders import InfantryCommander, CavalryCommander, ArtilleryCommander


class InfantryArmyFactory(AbstractArmyFactory):
    def create_unit(self) -> Infantry:
        return Infantry()

    def create_commander(self, name) -> InfantryCommander:
        return InfantryCommander(name)

    def __str__(self) -> str:
        return "Пехота"


class CavalryArmyFactory(AbstractArmyFactory):
    def create_unit(self) -> Cavalry:
        return Cavalry()

    def create_commander(self, name) -> CavalryCommander:
        return CavalryCommander(name)

    def __str__(self) -> str:
        return "Кавалерия"


class ArtilleryArmyFactory(AbstractArmyFactory):
    def create_unit(self) -> Artillery:
        return Artillery()

    def create_commander(self, name) -> ArtilleryCommander:
        return ArtilleryCommander(name)

    def __str__(self) -> str:
        return "Артиллерия"
