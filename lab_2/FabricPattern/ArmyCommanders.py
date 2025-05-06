from Commander import Commander


class InfantryCommander(Commander):
    def __init__(self, name):
        super().__init__(name)

    def command_attack(self):
        return "Пехота, огонь!!!"

    def command_defend(self):
        return "Пехота, отступаем в бункер!"

    def command_move(self):
        return "Пехота, движемся вперед!"

    def __str__(self) -> str:
        return f"Командир пехоты - {self._name}"


class CavalryCommander(Commander):
    def __init__(self, name):
        super().__init__(name)

    def command_attack(self) -> str:
        return "Кавалерия, в атаку!!!"

    def command_defend(self) -> str:
        return "Кавалерия, отступаем в лес!"

    def command_move(self) -> str:
        return "Кавалерия, скачем прямо!"

    def __str__(self) -> str:
        return f"Командир кавалерии - {self._name}"


class ArtilleryCommander(Commander):
    def __init__(self, name):
        super().__init__(name)

    def command_attack(self) -> str:
        return "Артиллерия, цельсь... огонь!!!"

    def command_defend(self) -> str:
        return "Артиллерия, отступаем в окопы!"

    def command_move(self) -> str:
        return "Артиллерия, по машинам!"

    def __str__(self) -> str:
        return f"Командир артиллерии - {self._name}"
