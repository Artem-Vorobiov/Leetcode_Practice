import unittest
from lengthOfLongestSubstring import Solution

class TestLengthOfLongestSubstring(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        s = "abcabcbb"
        expected = 3
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)

    def test_case_2(self):
        s = "bbbbb"
        expected = 1 
        self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)
        
if __name__ == "__main__":
    unittest.main()