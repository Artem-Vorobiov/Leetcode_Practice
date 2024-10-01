import unittest
from ransomNote import Solution

class TestRansomNote(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        ransomNote = "a"
        magazine = "b"
        expected = False
        self.assertEqual(self.solution.canConstruct(ransomNote, magazine), expected)

    def test_case_2(self):
        ransomNote = "aa"
        magazine = "ab"
        expected = False
        self.assertEqual(self.solution.canConstruct(ransomNote, magazine), expected)

    def test_case_3(self):
        ransomNote = "aabb"
        magazine = "abglkhjmgkab"
        expected = True
        self.assertEqual(self.solution.canConstruct(ransomNote, magazine), expected)
    
if __name__ == "__main__":
    unittest.main()