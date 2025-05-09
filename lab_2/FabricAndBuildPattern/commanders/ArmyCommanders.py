from lab_2.FabricAndBuildPattern.commanders.Commander import Commander


class InfantryCommander(Commander):
    def __init__(self, name: str):
        super().__init__(name)

    def command_attack(self) -> str:
        return f"Пехота, огонь!!!\n{super().command_attack()}"

    def command_defend(self):
        return f"Пехота, отступаем в бункер!\n{super().command_defend()}"

    def command_move(self):
        return f"Пехота, движемся вперед!\n{super().command_move()}"

    def __str__(self) -> str:
        return f"Командир пехоты - {self._name} (войск: {self.get_unit_count()})"


class CavalryCommander(Commander):
    def __init__(self, name):
        super().__init__(name)

    def command_attack(self) -> str:
        return f"Кавалерия, в атаку!!!\n{super().command_attack()}"

    def command_defend(self) -> str:
        return f"Кавалерия, отступаем в лес!\n{super().command_defend()}"

    def command_move(self) -> str:
        return f"Кавалерия, скачем прямо!\n{super().command_move()}"

    def __str__(self) -> str:
        return f"Командир кавалерии - {self._name} (войск: {self.get_unit_count()})"


class ArtilleryCommander(Commander):
    def __init__(self, name):
        super().__init__(name)

    def command_attack(self) -> str:
        return f"Артиллерия, цельсь... огонь!!!\n{super().command_attack}"

    def command_defend(self) -> str:
        return f"Артиллерия, отступаем в окопы!{super().command_defend()}"

    def command_move(self) -> str:
        return f"Артиллерия, по машинам!\n{super().command_move()}"

    def __str__(self) -> str:
        return f"Командир артиллерии - {self._name} (войск: {self.get_unit_count()})"
