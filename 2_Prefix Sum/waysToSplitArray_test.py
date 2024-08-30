import unittest
from waysToSplitArray import Solution  

class TestWaysToSplitArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [1, 2, 3, 4, 5]
        expected = 3  # Valid splits: [1, 2, 3] | [4, 5], [1, 2, 3, 4] | [5], [1, 2, 3, 4, 5] | []
        self.assertEqual(self.solution.waysToSplitArray(nums), expected)

    def test_case_2(self):
        nums = [1, 2]
        expected = 1  # Valid split: [1] | [2]
        self.assertEqual(self.solution.waysToSplitArray(nums), expected)

    def test_case_3(self):
        nums = [4, 4, 4, 4]
        expected = 3  # Valid splits: [4] | [4, 4, 4], [4, 4] | [4, 4], [4, 4, 4] | [4]
        self.assertEqual(self.solution.waysToSplitArray(nums), expected)

if __name__ == '__main__':
    unittest.main()
