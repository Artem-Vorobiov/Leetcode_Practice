import unittest
from findMaxLength import Solution  # Replace 'your_solution_file' with the actual filename without '.py'

class TestFindMaxLength(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [0, 1, 0, 1, 0, 1, 1, 0]
        expected = 8  # The entire array has an equal number of 0s and 1s
        self.assertEqual(self.solution.findMaxLength(nums), expected)

    def test_case_2(self):
        nums = [0, 0, 0, 0, 0]
        expected = 0  # No subarray with equal number of 0s and 1s
        self.assertEqual(self.solution.findMaxLength(nums), expected)


if __name__ == '__main__':
    unittest.main()
