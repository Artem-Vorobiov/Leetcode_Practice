import unittest
from longestOnes import Solution  # Replace 'your_solution_file' with the actual filename without '.py'

class TestLongestOnes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [1, 1, 0, 0, 1, 1, 0, 1, 1]
        k = 2
        expected = 9  # The longest subarray with at most 2 zeros is [1, 1, 0, 0, 1, 1, 0, 1, 1]
        self.assertEqual(self.solution.longestOnes(nums, k), expected)

    def test_case_2(self):
        nums = [1, 1, 1, 1, 1, 1, 1]
        k = 3
        expected = 7  # No zeros in the array, so the length of the entire array is the answer
        self.assertEqual(self.solution.longestOnes(nums, k), expected)

    def test_case_3(self):
        nums = [0, 0, 0, 0, 0]
        k = 2
        expected = 3  # The longest subarray with exactly 2 zeros is [0, 0, 0] (or any 3 continuous zeros)
        self.assertEqual(self.solution.longestOnes(nums, k), expected)

if __name__ == '__main__':
    unittest.main()
