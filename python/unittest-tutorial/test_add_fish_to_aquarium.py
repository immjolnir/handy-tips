import unittest

def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"tank_a": fish_list}


class TestAddFishToAquarium(unittest.TestCase):
    def test_add_fish_to_aquarium_success(self):
        actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["shark", "tuna"]}
        expected = {"tank_a": ["rabbit"]} # failure cause
        self.assertEqual(actual, expected)

# $ python3 -m unittest test_add_fish_to_aquarium.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
