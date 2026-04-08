#!/usr/bin/env python3


class GardenError(Exception):
    """Base exception for garden problems."""
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    """Exception for plant problems."""
    def __init__(self, message="A plant is experiencing problems"):
        super().__init__(message)


class WaterError(GardenError):
    """Exception for watering problems."""
    def __init__(self, message="Water system malfunction detected"):
        super().__init__(message)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}")

    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught {type(e).__name__}: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
