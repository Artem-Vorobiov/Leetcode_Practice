import unittest
from wordPattern import Solution

class TestwordPattern(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        input = ["abba", "dog cat cat dog"]
        expected = True
        self.assertEqual(self.solution.wordPattern(input[0], input[1]), expected)

    def test_case_2(self):
        input = ["abba", "dog cat cat fish"]
        expected = False
        self.assertEqual(self.solution.wordPattern(input[0], input[1]), expected)

    def test_case_3(self):
        input = ["e", "eukera"]
        expected = True
        self.assertEqual(self.solution.wordPattern(input[0], input[1]), expected)

if __name__ == "__main__":
    unittest.main()