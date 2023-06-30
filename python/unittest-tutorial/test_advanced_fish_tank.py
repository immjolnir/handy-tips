# using the tearDown Method to Clean Up Resources
#
# The setUp method creates an AdvancedFishTank instance and assigns it to self.fish_tank. The tearDown method calls the empty_tank method on self.fish_tank: this ensures that the fish_tank.txt file is removed after each test method runs. This way, each test starts with a clean slate. The test_fish_tank_writes_file method verifies that the default contents of "shark, tuna" are written to the fish_tank.txt file.

import os
import unittest

class AdvancedFishTank:
    def __init__(self):
        self.fish_tank_file_name = "fish_tank.txt"
        default_contents = "shark, tuna"
        with open(self.fish_tank_file_name, "w") as f:
            f.write(default_contents)

    def empty_tank(self):
        os.remove(self.fish_tank_file_name)


class TestAdvancedFishTank(unittest.TestCase):
    def setUp(self):
        self.fish_tank = AdvancedFishTank()

    def tearDown(self):
        self.fish_tank.empty_tank()

    def test_fish_tank_writes_file(self):
        with open(self.fish_tank.fish_tank_file_name) as f:
            contents = f.read()
        self.assertEqual(contents, "shark, tuna")
