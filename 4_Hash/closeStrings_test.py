import unittest
from closeStrings import Solution

class closeStringsTEST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        input = ['abbzzca', 'babzzcz']
        output = False
        self.assertEqual(self.solution.closeStrings(input[0], input[1]), output)

    def test_case_2(self):
        input = ['abc', 'bca']
        output = True
        self.assertEqual(self.solution.closeStrings(input[0], input[1]), output)

    def test_case_3(self):
        input = ['cabbba', 'abbccc']
        output = True
        self.assertEqual(self.solution.closeStrings(input[0], input[1]), output)


if __name__ == "__main__":
    unittest.main()