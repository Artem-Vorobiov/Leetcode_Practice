import unittest
from runningSum import Solution  

class TestRunningSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [1, 2, 3, 4]
        expected = [1, 3, 6, 10]  # Running sum calculation: [1, 1+2, 1+2+3, 1+2+3+4]
        self.assertEqual(self.solution.runningSum(nums), expected)

    def test_case_2(self):
        nums = [1, -1, 2, -2, 3]
        expected = [1, 0, 2, 0, 3]  # Running sum calculation: [1, 1-1, 1-1+2, 1-1+2-2, 1-1+2-2+3]
        self.assertEqual(self.solution.runningSum(nums), expected)

    def test_case_3(self):
        nums = [5]
        expected = [5]  # Running sum calculation: [5]
        self.assertEqual(self.solution.runningSum(nums), expected)

if __name__ == '__main__':
    unittest.main()
