def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    valid_input = "25"
    print(f"Input data is '{valid_input}'")
    try:
        temp = input_temperature(valid_input)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print()

    invalid_input = "abc"
    print(f"Input data is '{invalid_input}'")
    try:
        temp = input_temperature(invalid_input)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()