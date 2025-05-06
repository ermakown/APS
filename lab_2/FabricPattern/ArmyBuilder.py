from AbstractArmyFactory import AbstractArmyFactory


class ArmyBuilder:
    def __init__(self, factory: AbstractArmyFactory):
        self._army = factory
        self._commander = None
        self._units = list()

    def add_units(self) -> list:
        count = int(input("Введите количество бойцов: "))
        for i in range(count):
            name = input("Введите фамилию бойца: ")
            self._army._units.append(name)
        return self._army._units

    def review_units(self) -> None:
        for i in self._units:
            print(f"Военный - {i}", sep="\n")

    def add_commander(self) -> str:
        name = input("Введите имя и фамилию командира: ")
        self._commander = self._army.create_commander(name)
        return f"Командир - {self._commander}"

    def __str__(self) -> str: ...
