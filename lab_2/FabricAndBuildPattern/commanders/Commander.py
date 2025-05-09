from lab_2.FabricAndBuildPattern.units.Unit import Unit


class Commander:
    def __init__(self, name: str):
        self._name = name
        self._units: list[Unit] = []

    def add_unit(self, unit: Unit) -> None:
        self._units.append(unit)

    def get_unit_count(self) -> int:
        return len(self._units)

    def command_attack(self) -> str:
        if not self._units:
            return "Армия пуста!"
        return self._units[0].attack()

    def command_defend(self) -> str:
        if not self._units:
            return "Армия пуста!"
        return self._units[0].defend()

    def command_move(self) -> str:
        if not self._units:
            return "Армия пуста!"
        return self._units[0].move()
