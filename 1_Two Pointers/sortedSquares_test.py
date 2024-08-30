# test_sorted_squares.py
import unittest
from sortedSquares import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_sorted_squares(self):
        # Test case 1: Mix of negative and positive numbers
        nums = [-4, -1, 0, 3, 10]
        expected = [0, 1, 9, 16, 100]
        result = self.solution.sortedSquares(nums)
        self.assertEqual(result, expected)

        # Test case 2: All negative numbers
        nums = [-7, -3, -1]
        expected = [1, 9, 49]
        result = self.solution.sortedSquares(nums)
        self.assertEqual(result, expected)

        # Test case 3: All positive numbers
        nums = [1, 2, 3, 5]
        expected = [1, 4, 9, 25]
        result = self.solution.sortedSquares(nums)
        self.assertEqual(result, expected)

        # Test case 4: Mix of negative and positive numbers with duplicates
        nums = [-5, -3, -2, -1, 4, 4]
        expected = [1, 4, 9, 16, 16, 25]
        result = self.solution.sortedSquares(nums)
        self.assertEqual(result, expected)

        # Test case 5: Single element array
        nums = [3]
        expected = [9]
        result = self.solution.sortedSquares(nums)
        self.assertEqual(result, expected)

        # Test case 6: Empty array
        nums = []
        expected = []
        result = self.solution.sortedSquares(nums)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
