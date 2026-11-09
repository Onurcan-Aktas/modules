def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print("")
    readings = ("25", "abc", "100", "-50")
    for reading in readings:
        print(f"Input data is '{reading}'")
        try:
            print(f"Temperature is now {input_temperature(reading)}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()