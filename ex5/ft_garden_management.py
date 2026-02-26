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


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name: str) -> None:
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")

        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")

        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")

        except Exception as e:
            print(f"Error during watering: {e}")

        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str,
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

        return (f"{plant_name}: healthy (water: {water_level}, "
                f"sun: {sunlight_hours})\n")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")

    garden = GardenManager()

    # Test 1: Adding plants
    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato")
        garden.add_plant("lettuce")
        garden.add_plant("")  # This will raise PlantError
    except PlantError as e:
        print(f"Error adding plant: {e}")

    # Test 2: Watering plants (with cleanup)
    print("\nWatering plants...")
    garden.water_plants()

    # Test 3: Checking plant health
    print("\nChecking plant health...")
    try:
        result = garden.check_plant_health("tomato", 5, 8)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result = garden.check_plant_health("lettuce", 15, 8)  # Bad water
        print(result)
    except ValueError as e:
        print(f"Error checking lettuce: {e}")

    # Test 4: Error recovery
    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
