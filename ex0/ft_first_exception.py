#!/usr/bin/env python3


def check_temperature(temp_str: str) -> float:
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        return temp
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
        return temp
    else:
        print(f"Temperature {temp}°C is perfect for plants!\n")
        return temp


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")
    tests = ["25", "abc", "100", "-50"]
    for temp in tests:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
