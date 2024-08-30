# test_reverse_prefix.py
import unittest
from reversePrefix import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_reverse_prefix_found(self):
        # Test case 1: Character exists in the middle
        word = "abcdefd"
        ch = "d"
        expected = "dcbaefd"
        result = self.solution.reversePrefix(word, ch)
        self.assertEqual(result, expected)

        # Test case 2: Character is the first character
        word = "zabcd"
        ch = "z"
        expected = "zabcd"
        result = self.solution.reversePrefix(word, ch)
        self.assertEqual(result, expected)

        # Test case 3: Character is the last character
        word = "abcdz"
        ch = "z"
        expected = "zdcba"
        result = self.solution.reversePrefix(word, ch)
        self.assertEqual(result, expected)

        # Test case 4: Multiple occurrences of character
        word = "aaxxxa"
        ch = "x"
        expected = "xaaxxa"
        result = self.solution.reversePrefix(word, ch)
        self.assertEqual(result, expected)

    def test_reverse_prefix_not_found(self):
        # Test case 5: Character does not exist
        word = "abcdef"
        ch = "z"
        expected = "abcdef"
        result = self.solution.reversePrefix(word, ch)
        self.assertEqual(result, expected)

    def test_reverse_prefix_empty_string(self):
        # Test case 6: Empty string
        word = ""
        ch = "a"
        expected = ""
        result = self.solution.reversePrefix(word, ch)
        self.assertEqual(result, expected)

    def test_reverse_prefix_single_character(self):
        # Test case 7: Single character string where character matches
        word = "a"
        ch = "a"
        expected = "a"
        result = self.solution.reversePrefix(word, ch)
        self.assertEqual(result, expected)

        # Test case 8: Single character string where character does not match
        word = "b"
        ch = "a"
        expected = "b"
        result = self.solution.reversePrefix(word, ch)
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
