from lab_2.FabricPattern.Unit import Unit


class Infantry(Unit):
    def attack(self) -> str:
        return "Пехота обстреливает автоматами!"

    def defend(self) -> str:
        return "Пехота прячется в бункере!"

    def move(self) -> str:
        return "Пехота передвигается пешком!"


class Cavalry(Unit):
    def attack(self) -> str:
        return "Кавалерия атакует холодным оружием!"

    def defend(self) -> str:
        return "Кавалерия прячется в лесу!"

    def move(self) -> str:
        return "Кавалерия передвигается на лошадях!"


class Artillery(Unit):
    def attack(self) -> str:
        return "Артиллерия атакует с помощью военных машин!"

    def defend(self) -> str:
        return "Артиллерия укрывается в окопах для орудий!"

    def move(self) -> str:
        return "Артиллерия передвигается на военных машинах и грузовиках!"
