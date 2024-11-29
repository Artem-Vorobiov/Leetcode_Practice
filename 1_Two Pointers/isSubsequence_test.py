import unittest
from isSubsequence import Solution

class Solution_TEST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_case_1(self):
        input = ["axc", "ahbgdc"]
        expected = False
        self.assertEqual(self.solution.isSubsequence(input[0], input[1]), expected)

    def test_case_2(self):
        input = ["abc", "ahbgdc"]
        expected = True
        self.assertEqual(self.solution.isSubsequence(input[0], input[1]), expected)


if __name__ == "__main__":
    unittest.main()
