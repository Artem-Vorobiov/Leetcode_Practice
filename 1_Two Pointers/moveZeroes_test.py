import unittest
from moveZeroes import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_move_zeroes_basic(self):
        # Test case 1: A mix of zeros and non-zero numbers
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

        # Test case 2: An array with no zeros
        nums = [1, 2, 3, 4]
        expected = [1, 2, 3, 4]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

        # Test case 3: An array with all zeros
        nums = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_move_zeroes_edge_cases(self):
        # Test case 4: An empty array
        nums = []
        expected = []
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

        # Test case 5: A single element array (non-zero)
        nums = [1]
        expected = [1]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)


if __name__ == '__main__':
    unittest.main()
