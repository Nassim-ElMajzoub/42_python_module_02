#!/usr/bin/env python3


def garden_operations() -> None:
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt", "r")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("\nTesting KeyError...")
    try:
        plants = {"rose": 5, "oak": 10}
        plants["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        int("not_a_number")
    except (ValueError, ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


def test_error_types() -> None:
    garden_operations()


if __name__ == "__main__":
    test_error_types()
