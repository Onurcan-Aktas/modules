class GardenError(Exception):
    def __init__(self, message: str = "General garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def trigger_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def trigger_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    for description, trigger in (("PlantError", trigger_plant_error),
                                 ("WaterError", trigger_water_error)):
        print(f"Testing {description}...")
        try:
            trigger()
        except GardenError as error:
            print(f"Caught GardenError: {error}")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
