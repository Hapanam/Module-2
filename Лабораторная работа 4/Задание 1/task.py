# TODO: описать базовый класс
class Animal:
    def __init__(self, name: str, species: str):
        self._name = name
        self._species = species

    @property
    def name(self) -> str:
        return self._name

    @property
    def species(self) -> str:
        return self._species

    def sound(self) -> str:
        return "Рычание"

    def __str__(self) -> str:
        return f"Животное {self.name}, вид {self.species}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, species={self.species!r})"

# TODO: описать дочерний класс
class Mammal(Animal):
    def __init__(self, name: str, species: str, fur_color: str):
        super().__init__(name, species)
        self._fur_color = fur_color

    @property
    def fur_color(self) -> str:
        return self._fur_color

    def sound(self) -> str:
        return "Мычание"

    def __str__(self) -> str:
        return f"Млекопитающее {self.name}, вид {self.species}, цвет шерсти {self.fur_color}"

class Bird(Animal):
    def __init__(self, name: str, species: str, wing_span: float):
        super().__init__(name, species)
        self._wing_span = wing_span

    @property
    def wing_span(self) -> float:
        return self._wing_span

    def sound(self) -> str:
        return "Чириканье"

    def __str__(self) -> str:
        return f"Птица {self.name}, вид {self.species}, размах крыльев {self.wing_span} м"