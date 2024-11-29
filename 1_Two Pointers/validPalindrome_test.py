import unittest

from validPalindrome import (
    Solution,  # Import the Solution class from validPalindrome.py
)


class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_one_removal_palindrome(self):
        # Test case where the string can become a palindrome by removing one character
        self.assertTrue(self.solution.validPalindrome("abca"))

    def test_non_palindrome(self):
        # Test case where the string cannot be made a palindrome by removing one character
        self.assertFalse(self.solution.validPalindrome("abcdefg"))


if __name__ == "__main__":
    unittest.main()
