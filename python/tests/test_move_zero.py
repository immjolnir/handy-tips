import unittest

class MoveZero:

    @classmethod
    def run(cls, data):
        """Python always uses pass-by-reference values.
        So the 'data' will be passed as reference value too.
        """
        for index, element in enumerate(data):
            if element == 0: # find the first zero
                j = index + 1
                while j < len(data) - 1 and data[j] == 0: # find the first non-zero
                    j += 1

                if j <= len(data) - 1:
                    # swap index and j
                    print("swap:{}, {}. {}<=>{}".format(index, j, data[index], data[j]))
                    data[index], data[j] = data[j], data[index]

class MoveZeroTestCase(unittest.TestCase):
    def test_positive_case(self):
        DATA = [0, 1, 0, 3, 12]
        RESULT = [1, 3, 12, 0, 0 ]

        actual = DATA.copy()
        MoveZero.run(actual)
        self.assertEqual(actual, RESULT)  # add assertion here

    def test_only0_case(self):
        DATA = [0]
        RESULT = [0]

        actual = DATA.copy()
        MoveZero.run(actual)
        self.assertEqual(actual, RESULT)  # add assertion here

    def test_all0_case(self):
        DATA = [0, 0, 0, 0, 0]
        RESULT = [0, 0, 0, 0, 0 ]

        actual = DATA.copy()
        MoveZero.run(actual)
        self.assertEqual(actual, RESULT)  # add assertion here

    def test_not_contain0_case(self):
        DATA = [1, 2, 3, 4, 5]
        RESULT = [1, 2, 3, 4, 5]

        actual = DATA.copy()
        MoveZero.run(actual)
        self.assertEqual(actual, RESULT)  # add assertion here

if __name__ == '__main__':
    unittest.main()

