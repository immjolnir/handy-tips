# test a function that raises an exception
# test_add_fish_to_aquarium_exception uses the with self.assertRaises(...) context manager provided by TestCase to check that add_fish_to_aquarium rejects the inputted list as too long. The first argument to self.assertRaises is the Exception class that we expect to be raised—in this case, ValueError. The self.assertRaises context manager is bound to a variable named exception_context. The exception attribute on exception_context contains the underlying ValueError that add_fish_to_aquarium raised. When we call str() on that ValueError to retrieve its message, it returns the correct exception message we expected.

import unittest

def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"tank_a": fish_list}


class TestAddFishToAquarium(unittest.TestCase):
    def test_add_fish_to_aquarium_success(self):
        actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["shark", "tuna"]}
        self.assertEqual(actual, expected)

    def test_add_fish_to_aquarium_exception(self):
        too_many_fish = ["shark"] * 25
        with self.assertRaises(ValueError) as exception_context:
            add_fish_to_aquarium(fish_list=too_many_fish)
        self.assertEqual(
            str(exception_context.exception),
            "A maximum of 10 fish can be added to the aquarium"
        )
