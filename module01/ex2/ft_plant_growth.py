class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")

    def grow(self, amount: float = 0.7) -> None:
        self.height += amount

    def age(self) -> None:
        self.plant_age += 1


def main() -> None:
    plant = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    plant.show()
    starting_height = plant.height
    for day in range(1, 8):
        plant.grow()
        plant.age()
        print(f"=== Day {day} ===")
        plant.show()
    print(f"Growth this week: {(plant.height - starting_height):.1f}cm")


if __name__ == "__main__":
    main()
