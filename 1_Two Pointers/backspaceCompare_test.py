import unittest
from backspaceCompare import Solution

class backspaceCompareTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        input = ["ab#c", "ad#c"]
        output = True
        self.assertEqual(self.solution.backspaceCompare(input[0],input[1]), output)

    def test_case_2(self):
        input =["a#c", "b"]
        output = False
        self.assertEqual(self.solution.backspaceCompare(input[0], input[1]), output)


if __name__ == '__main__':
    unittest.main()