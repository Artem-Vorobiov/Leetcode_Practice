import unittest
from numSubarrayProductLessThanK import Solution

class TestnumSubarrayProductLessThanK(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        input = [[10,5,2,6],100]
        expected = 8
        self.assertEqual(self.solution.numSubarrayProductLessThanK(input[0],input[1]), expected)

    def test_case_2(self):
        input = [[1,2,3], 0]
        expected = 0 
        self.assertEqual(self.solution.numSubarrayProductLessThanK(input[0],input[1]), expected)

    def test_case_3(self):
        input = [[1,1,1,1,1], 1]
        expected = 0
        self.assertEqual(self.solution.numSubarrayProductLessThanK(input[0], input[1]), expected)

if __name__ == "__main__":
    unittest.main()