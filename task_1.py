# TODO: Подробно описать три произвольных класса
import doctest

# TODO: описать класс
class Tree:
    def init(self, height: float, age: int, species: str):
        if height <= 0:
            raise ValueError("Height is not a positive number")
        if age < 0:
            raise ValueError("Age is not a positive number")
        self.height = height
        self.age = age
        self.species = species

    def grow(self, years: int = 1) -> None:
        if years <= 0:
            raise ValueError("Years must be positive.")

        self.age += years
        self.height += years * 0.5

    def describe(self) -> str:
        return f"The tree is a {self.species}, {self.height} meters tall, and {self.age} years old."

# TODO: описать ещё класс
class Car:
    def init(self, brand: str, max_speed: float, fuel_capacity: float):
        if max_speed <= 0:
            raise ValueError("Speed is not a positive number")
        if fuel_capacity <= 0:
            raise ValueError("Fuel is not a positive number")

        self.brand = brand
        self.max_speed = max_speed
        self.fuel_capacity = fuel_capacity

    def refuel(self, liters: float) -> None:
        if liters <= 0:
            raise ValueError("Liters are not a positive number")
        if liters > self.fuel_capacity:
            raise ValueError("Exceeds tank capacity")
        print(f"Added {liters} liters of fuel.")

    def upgrade_speed(self, increase: float) -> None:
        if increase <= 0:
            raise ValueError("Speed is not a positive number")
        self.max_speed += increase
        print(f"Max speed upgraded to {self.max_speed} km/h")

# TODO: и ещё один
class Student:
    def init(self, name: str, age: int, grades: list[float]):
        if not (6 <= age <= 18):
            raise ValueError("Not school age")
        if not all(0 <= grade <= 100 for grade in grades):
            raise ValueError("Grades are out of range")
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade: float) -> None:
        if not (0 <= grade <= 100):
            raise ValueError("Grades are out of range")

        self.grades.append(grade)

    def calculate_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def describe(self) -> str:
        average_grade = self.calculate_average()
        return f"{self.name}, {self.age} years old, has an average grade of {average_grade:.1f}."

if __name__ == "__main__":
    doctest.testmod()