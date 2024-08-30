import unittest
from minStartValue import Solution  

class TestMinStartValue(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [-3, 2, -3, 4, 2]
        expected = 5  # Minimum start value to keep running sum always >= 1
        self.assertEqual(self.solution.minStartValue(nums), expected)

    def test_case_2(self):
        nums = [1, 2, 3, 4]
        expected = 1  # All positive numbers, so start value of 1 is enough
        self.assertEqual(self.solution.minStartValue(nums), expected)

    def test_case_3(self):
        nums = [-1, -2, -3]
        expected = 7  # Minimum start value to ensure the running sum never drops below 1
        self.assertEqual(self.solution.minStartValue(nums), expected)

if __name__ == '__main__':
    unittest.main()
