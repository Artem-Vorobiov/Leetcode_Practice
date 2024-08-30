import unittest
from maxNumerPatter import Solution  

class TestMaxNumberOfPatternInstances(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        text = "loonbalxballpoon"
        pattern = "balloon"
        expected = 2  # The word "balloon" can be formed twice: "balloon", "balloon"
        self.assertEqual(self.solution.maxNumberOfBalloons(text, pattern), expected)

    def test_case_2(self):
        text = "abcde"
        pattern = "balloon"
        expected = 0  # Missing characters needed to form "balloon" (specifically 'l', 'o', and 'n')
        self.assertEqual(self.solution.maxNumberOfBalloons(text, pattern), expected)

    def test_case_3(self):
        text = "balon"
        pattern = "balloon"
        expected = 0  # Not enough 'l' and 'o' characters to form even one "balloon"
        self.assertEqual(self.solution.maxNumberOfBalloons(text, pattern), expected)

if __name__ == '__main__':
    unittest.main()
