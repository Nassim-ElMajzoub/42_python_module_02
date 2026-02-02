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


