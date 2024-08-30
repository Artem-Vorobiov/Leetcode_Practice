import unittest
from getAverages import Solution  

class TestGetAverages(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [1, 3, 5, 7, 9, 11, 13, 15]
        k = 2
        expected = [-1, -1, 5, 7, 9, 11, -1, -1]  # Window size is 5; average for the valid windows
        self.assertEqual(self.solution.getAverages(nums, k), expected)

    def test_case_2(self):
        nums = [1, 2, 3]
        k = 5
        expected = [-1, -1, -1]  # Window size is 11, which is larger than the array length
        self.assertEqual(self.solution.getAverages(nums, k), expected)

    def test_case_3(self):
        nums = [4, 5, 6, 7]
        k = 0
        expected = [4, 5, 6, 7]  # Window size is 1; should return the original array
        self.assertEqual(self.solution.getAverages(nums, k), expected)

if __name__ == '__main__':
    unittest.main()
