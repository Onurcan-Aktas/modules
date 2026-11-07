class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = float(height)
        self._age = age

    def grow(self, grow_amount: float = 1.0) -> None:
        self._height += grow_amount

    def age(self, days: int = 1) -> None:
        self._age += days

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        shade_length = self._height * 1.5
        print(
            f"Tree {self._name} now produces a shade of {shade_length:.1f}cm "
            f"long and {self._trunk_diameter:.1f}cm wide."
        )


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0.0

    def grow(self, grow_amount: float = 1.0) -> None:
        super().grow(grow_amount)
        self._nutritional_value += grow_amount

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value:.1f}")



    


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.bloom()
    flower.show()
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    tree.produce_shade()
    tomato = Vegetable("Tomato", 8.0, 10, "April")
    tomato.show()
    tomato.grow(19.0)
    tomato.age(20)
    tomato.show()
