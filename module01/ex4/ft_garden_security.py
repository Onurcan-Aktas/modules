class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0

        if height >= 0:
            self._height = float(height)
        else:
            print(f"{self._name}:Error, height can't be negative")

        if age >= 0:
            self._age = age
        else:
            print(f"{self._name}: Error, age can't be negative")

        print(
            f"Plant created:{
                self._name}: {
                self._height:.1f}cm, {
                self._age} days old")

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = float(new_height)
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def current_state(self) -> None:
        print(f"Current state: {self._name}: {self._height:.1f}cm, "
              f"{self._age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 32, 32)
    rose.get_age()
    rose.get_height()
    rose.set_age(55)
    rose.set_height(76)
    rose.get_height()
    rose.get_age()
    papatya = Plant("papatya", -32, -32)
    papatya.set_height(-32)
    papatya.set_age(-32)
    rose.current_state()
    papatya.current_state()
