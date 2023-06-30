# Using the setUp method to create Resouces
# Since setUp is run before every individual test method, a new FishTank instance is instantiated for both test_fish_tank_empty_by_default and test_fish_tank_can_be_filled.

import unittest

class FishTank:
    def __init__(self):
        self.has_water = False

    def fill_with_water(self):
        self.has_water = True

class TestFishTank(unittest.TestCase):
    def setUp(self):
        print("call setUp\n") # print it twice
        self.fish_tank = FishTank()

    def test_fish_tank_empty_by_default(self):
        self.assertFalse(self.fish_tank.has_water)

    def test_fish_tank_can_be_filled(self):
        self.fish_tank.fill_with_water()
        self.assertTrue(self.fish_tank.has_water)
