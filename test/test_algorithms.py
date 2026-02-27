import unittest
from array_search import algorithms


arrays = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1],
    [2],
    [1, 2],
    [2, 4, 6],
    [1, 3, 5, 7, 9],
    [2, 4, 6, 8, 10],
    [10, 20, 30, 40, 50],
    [-99, -50, -10, 0, 10, 50, 99],
    [],
]


elements = [5, 1, 2, 2, 4, 5, 8, 30, -10, 0]


expected_index = [4, 0, 0, 1, 1, 2, 3, 2, 2, -1]


class AlgorithmsTests(unittest.TestCase):
    def test_linear_search(self):

        for i in range(len(arrays)):
            result = algorithms.linear_search(arrays[i], elements[i])
            self.assertEqual(result, expected_index[i])
    def test_binary_search(self):
        for i in range(len(arrays)):
            result = algorithms.binary_search(arrays[i], elements[i])
            self.assertEqual(result, expected_index[i])
    def test_ternary_search(self):
        for i in range(len(arrays)):
            result = algorithms.ternary_search(arrays[i], elements[i])
            self.assertEqual(result, expected_index[i])


if __name__ == "__main__":
    unittest.main(verbosity=2)
