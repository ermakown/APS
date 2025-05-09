from lab_2.FabricAndBuildPattern.units.Unit import Unit


class Infantry(Unit):
    def attack(self) -> str:
        return "Пехота атакует в ближнем бою!"

    def defend(self) -> str:
        return "Пехота укрепляется и обороняется"

    def move(self) -> str:
        return "Пехота марширует по земле"


class Cavalry(Unit):
    def attack(self) -> str:
        return "Кавалерия наносит удар в стремительном налёте!"

    def defend(self) -> str:
        return "Кавалерия отступает и перегруппировывается"

    def move(self) -> str:
        return "Кавалерия быстро перемещается по полю"


class Artillery(Unit):
    def attack(self) -> str:
        return "Артиллерия ведёт обстрел с дальнего расстояния!"

    def defend(self) -> str:
        return "Артиллерия прикрывается огнём и сменой позиции"

    def move(self) -> str:
        return "Артиллерия перемещается медленно с помощью техники"
