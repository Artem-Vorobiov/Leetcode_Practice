# test_prefix_sum.py
import unittest
from two_sum import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_two_sum(self):
        # Test case 1
        nums = [2, 7, 11, 15]
        target = 9
        expected = [1, 0]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected)

        # Test case 2
        nums = [3, 2, 4]
        target = 6
        expected = [2, 1]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected)

        # Test case 3
        nums = [3, 3]
        target = 6
        expected = [1, 0]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected)

    def test_two_sum_no_solution(self):
        # Test case where no solution is possible
        nums = [1, 2, 3]
        target = 7
        result = self.solution.twoSum(nums, target)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
