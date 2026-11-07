class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")




if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose=Plant("Rose", 25, 30)
    sunflower=Plant("Sunflower", 25, 30)
    cactus=Plant("Cactus", 25, 30)
    rose.show()
    sunflower.show()
    cactus.show()
