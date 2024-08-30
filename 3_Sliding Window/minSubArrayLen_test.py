import unittest
from minSubArrayLen import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_min_sub_array_len_basic(self):
        # Test case 1: A basic case with a valid subarray
        nums = [2, 3, 1, 2, 4, 3]
        target = 7
        expected = 2  # The subarray [4, 3] or [3, 4] has the minimal length
        result = self.solution.minSubArrayLen(target, nums)
        self.assertEqual(result, expected)

    def test_min_sub_array_len_no_subarray(self):
        # Test case 2: No subarray can meet the target
        nums = [1, 2, 3, 4, 5]
        target = 20
        expected = 0  # No subarray sums to 20
        result = self.solution.minSubArrayLen(target, nums)
        self.assertEqual(result, expected)

    def test_min_sub_array_len_single_element(self):
        # Test case 3: Single element equals to target
        nums = [7]
        target = 7
        expected = 1  # The single element meets the target
        result = self.solution.minSubArrayLen(target, nums)
        self.assertEqual(result, expected)

    def test_min_sub_array_len_large_elements(self):
        # Test case 4: Large numbers that sum quickly to target
        nums = [5, 1, 4, 3]
        target = 6
        expected = 1  # The subarray [5] or [4]
        result = self.solution.minSubArrayLen(target, nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
