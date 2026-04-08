#!/usr/bin/env python3


class PlantError(Exception):
    """Exception for plant problems."""
    def __init__(self, message="A plant is experiencing problems"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    try:
        print("=== Garden Watering System ===\n")
        print("Testing valid plants...")
        plants = ['Tomato', 'Lettuce', 'Carrots']
        try:
            print("Opening watering system")
            for plant in plants:
                water_plant(plant)
        except PlantError as e:
            print(f"Caught {type(e).__name__}: {e}")
            print(".. ending tests and returning to main")
            return
        finally:
            print("Closing watering system\n")

        print("Testing invalid plants...")
        plants = ['Tomato', 'lettuce', 'Carrots']
        try:
            print("Opening watering system")
            for plant in plants:
                water_plant(plant)
        except PlantError as e:
            print(f"Caught {type(e).__name__}: {e}")
            print(".. ending tests and returning to main")
            return
        finally:
            print("Closing watering system\n")
    finally:
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
