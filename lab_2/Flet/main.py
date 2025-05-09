import flet as ft
from lab_2.Flet.ArmyApp import ArmyApp


def main(page: ft.Page):
    ArmyApp(page)


if __name__ == "__main__":
    ft.app(target=main)
