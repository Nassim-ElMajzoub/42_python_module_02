#!/usr/bin/env python3


def check_plant_health(plant_name: str,
                       water_level: str, sunlight_hours: str) -> str:

    level = int(water_level)
    sunlight = int(sunlight_hours)

    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    elif level > 10:
        raise ValueError(f"Water level {level} "
                         f"is too high (max 10)")
    elif level < 1:
        raise ValueError(f"Water level {level} "
                         f"is too low (min 1)")
    elif sunlight > 12:
        raise ValueError(f"Sunlight hours {sunlight} "
                         f"is too high (max 12)")
    elif sunlight < 2:
        raise ValueError(f"Sunlight hours {sunlight} "
                         f"is too low (min 2)")

    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 5))
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing empty plant name...")
    try:
        print(check_plant_health(None, 5, 5))
    except ValueError as e:
        print(f"Error: {e}\n")

    print("Testing bad water level...")
    try:
        print(check_plant_health("tomato", 26, 5))
    except ValueError as e:
        print(f"Error: {e}\n")

    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 5, 1))
    except ValueError as e:
        print(f"Error: {e}\n")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
