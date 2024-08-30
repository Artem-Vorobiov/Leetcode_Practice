import unittest
from findMaxAverage import Solution  

class TestFindMaxAverage(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        expected = 12.75
        self.assertAlmostEqual(self.solution.findMaxAverage(nums, k), expected, places=5)


if __name__ == '__main__':
    unittest.main()