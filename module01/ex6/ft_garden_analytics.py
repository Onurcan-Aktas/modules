from typing import cast

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(
                f"Stats: {self.grow_calls} grow, {self.age_calls} age, "
                f"{self.show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = self._Stats()

    def grow(self, amount: float = 1.0) -> None:
        self._height += amount
        self._stats.grow_calls += 1

    def age(self, days: int = 1) -> None:
        self._age += days
        self._stats.age_calls += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")
        self._stats.show_calls += 1

    def _display_statistics(self) -> None:
        self._stats.display()

    @property
    def name(self) -> str:
        return self._name

    @staticmethod
    def is_older_than_a_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Anonymous plant", 0.0, 0)


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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seed_count = 0

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = 50

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seed_count}")


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_calls = 0

        def display(self) -> None:
            super().display()
            print(f"{self.shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats = self._TreeStats()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        shade_length = self._height * 1.5
        print(
            f"Tree {self._name} now produces a shade of {shade_length:.1f}cm "
            f"long and {self._trunk_diameter:.1f}cm wide."
        )
        stats = cast(Tree._TreeStats, self._stats)
        stats.shade_calls += 1


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant._display_statistics()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year old")
    print(f"Is 50 days more than a year?: {Plant.is_older_than_a_year(50)}")
    print(
        f"Is 400 days more than a year?: {
            Plant.is_older_than_a_year(400)}\n")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    display_stats(oak)
    sunflower = Seed("Sunflower", 40.0, 45, "yellow")
    sunflower.grow(60.0)
    sunflower.age(45)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_stats(anonymous)


if __name__ == "__main__":
    main()
