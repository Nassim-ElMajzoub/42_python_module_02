#!/usr/bin/env python3


class GardenError(Exception):
    """Base exception for garden problems."""
    pass


class PlantError(GardenError):
    """Exception for plant problems."""
    pass


class WaterError(GardenError):
    """Exception for watering problems."""
    pass


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")

    # Test 1: PlantError
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    # Test 2: WaterError
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    # Test 3: Catching all garden errors
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()

# class GardenError(Exception):
#     """Base exception for garden problems."""
#     def __init__(self, message="An unspecified garden problem occurred"):
#         self.message = message
#         super().__init__(self.message)


# class PlantError(GardenError):
#     """Exception for plant problems."""
#     def __init__(self, message="A plant is experiencing problems"):
#         self.message = message
#         super().__init__(self.message)


# class WaterError(GardenError):
#     """Exception for watering problems."""
#     def __init__(self, message="Water system malfunction detected"):
#         self.message = message
#         super().__init__(self.message)


# def test_custom_errors():
#     print("=== Custom Garden Errors Demo (Advanced) ===\n")

#     # Test 1: PlantError with custom message
#     print("Testing PlantError with custom message...")
#     try:
#         raise PlantError("The tomato plant is wilting!")
#     except PlantError as e:
#         print(f"Caught PlantError: {e}")

#     # Test 2: PlantError with DEFAULT message
#     print("\nTesting PlantError with default message...")
#     try:
#         raise PlantError()
#     except PlantError as e:
#         print(f"Caught PlantError: {e}")

#     # Test 3: WaterError with custom message
#     print("\nTesting WaterError with custom message...")
#     try:
#         raise WaterError("Not enough water in the tank!")
#     except WaterError as e:
#         print(f"Caught WaterError: {e}")

#     # Test 4: WaterError with DEFAULT message
#     print("\nTesting WaterError with default message...")
#     try:
#         raise WaterError()
#     except WaterError as e:
#         print(f"Caught WaterError: {e}")

#     # Test 5: Catching all garden errors
#     print("\nTesting catching all garden errors...")
#     try:
#         raise PlantError()
#     except GardenError as e:
#         print(f"Caught a garden error: {e}")

#     try:
#         raise WaterError("Tank is empty!")
#     except GardenError as e:
#         print(f"Caught a garden error: {e}")

#     print("\nAll custom error types work correctly!")


# if __name__ == "__main__":
#     test_custom_errors()
