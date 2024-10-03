import unittest
from fixedWindow import Solution

class TestFixedWindow(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        input = [[3, -1, 4, 12, -8, 5, 6], 4]
        expected = 18
        self.assertEqual(self.solution.fixedWindow(input[0], input[1]), expected)
    
    def test_case_2(self):
        input = [[1,3,2,5], 0]
        expected = False
        self.assertEqual(self.solution.fixedWindow(input[0], input[1]), expected)

    def test_case_3(self):
        input = [[0], 2]
        expected = False
        self.assertEqual(self.solution.fixedWindow(input[0], input[1]), expected)


if __name__ == '__main__':
    unittest.main()