# test_reverse_string.py
import unittest
from reverse_str import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_reverse_string(self):
        # Test case 1: Reverse a simple string
        s = ['h', 'e', 'l', 'l', 'o']
        expected = ['o', 'l', 'l', 'e', 'h']
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

        # Test case 2: Reverse a string with even number of characters
        s = ['H', 'a', 'n', 'n', 'a', 'h']
        expected = ['h', 'a', 'n', 'n', 'a', 'H']
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

        # Test case 3: Reverse a string with a single character
        s = ['A']
        expected = ['A']
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

        # Test case 4: Reverse an empty string
        s = []
        expected = []
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

if __name__ == '__main__':
    unittest.main()
