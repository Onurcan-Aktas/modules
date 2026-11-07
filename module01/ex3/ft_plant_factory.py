class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.show()

    def show(self) -> None:
        print(
            f"Created: {
                self.name}: {
                self.height:.1f}cm, {
                self.age} days old")


def main() -> None:
    print("=== Plant Factory Output ===")
    Plant("Rose", 25, 30)
    Plant("Oak", 200, 365)
    Plant("Cactus", 5, 90)
    Plant("Sunflower", 80, 45)
    Plant("Fern", 15, 120)


if __name__ == "__main__":
    main()
