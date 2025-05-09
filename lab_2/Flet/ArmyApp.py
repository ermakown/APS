import flet as ft

from lab_2.FabricAndBuildPattern.builder.ArmyFactories import (
    InfantryArmyFactory,
    CavalryArmyFactory,
    ArtilleryArmyFactory,
)
from lab_2.FabricAndBuildPattern.builder.ArmyBuilder import ArmyBuilder
from lab_2.FabricAndBuildPattern.commanders.Commander import Commander


class ArmyApp:
    def __init__(self, page: ft.Page):
        self._page = page
        self._page.title = "Армия"
        self._page.theme_mode = "system"
        self._page.padding = 30
        self._scroll = "adaptive"

        self._army_type = None
        self._commander = ft.TextField(label="Введите имя командира:", width=300)
        self._units = ft.TextField(
            label="Введите количество бойцов:",
            width=300,
            input_filter=ft.NumbersOnlyInputFilter(),
        )

        # self._infantry = ft.ElevatedButton("Пехота", on_click=)
        # self._cavalry = ft.ElevatedButton("Кавалерия", on_click= )
        # self._artillery = ft.ElevatedButton("Артиллерия", on_click= )

        self._logo = ft.Text(value="Армия", size=50)
        self._greetings = ft.Text(value="Добро пожаловать в создание армии! Выберите род войск из предложенных:", size=20)

        self._page.add(
            ft.Card(
                content=[self._logo]
            )
        )
