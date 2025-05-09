import sys
import os

from lab_2.FabricAndBuildPattern.builder.ArmyFactories import (
    InfantryArmyFactory,
    CavalryArmyFactory,
    ArtilleryArmyFactory,
)
from lab_2.FabricAndBuildPattern.builder.ArmyBuilder import ArmyBuilder
from lab_2.FabricAndBuildPattern.commanders.Commander import Commander

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


def simulate_battle(commander1: Commander, commander2: Commander):
    print("\n=== НАЧАЛО БИТВЫ ===")

    # Атака первой армии
    print(f"\n{commander1}:")
    print(commander1.command_attack())

    # Защита второй армии
    print(f"\n{commander2}:")
    print(commander2.command_defend())

    # Ответная атака
    print("\n=== ОТВЕТНЫЙ УДАР ===")
    print(f"\n{commander2}:")
    print(commander2.command_attack())

    # Защита первой армии
    print(f"\n{commander1}:")
    print(commander1.command_defend())


print("Добро пожаловать в создание армии!Выберете ряд войск!")

choice = int(input("пехота - 1, кавалерия - 2, артиллерия - 3: "))
factory = None
if choice == 1:
    factory = InfantryArmyFactory()
elif choice == 2:
    factory = CavalryArmyFactory()
else:
    factory = ArtilleryArmyFactory()

commander_name = input("введите имя командира: ")
count = int(input("введите количество борцов в армии: "))

builder1 = ArmyBuilder(factory, commander_name)
commander1 = builder1.add_units(count).build()

print("\nСоздаем вторую армию")

choice = int(input("пехота - 1, кавалерия - 2, артиллерия - 3: "))
factory = None
if choice == 1:
    factory = InfantryArmyFactory()
elif choice == 2:
    factory = CavalryArmyFactory()
else:
    factory = ArtilleryArmyFactory()

commander_name = input("введите имя командира: ")
count = int(input("введите количество борцов в армии: "))

builder2 = ArmyBuilder(factory, commander_name)
commander2 = builder2.add_units(count).build()

print("\n=== ВЫВОД ИНФОРМАЦИИ ОБ АРМИЯХ ===")
print(commander1)
print(commander2)

simulate_battle(commander1, commander2)
