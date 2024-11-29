import unittest
from shortestToChar import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        # Create an instance of Solution before every test case
        self.solution = Solution()

    def test_single_char_found(self):
        s = "loveleetcode"
        c = "e"
        # For the input string "loveleetcode" and character "e",
        # the expected output is the closest distance of each character to "e".
        expected_result = [3, 2, 1, 0, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2]
        self.assertEqual(self.solution.shortestToChar(s, c), expected_result)

    def test_character_not_found(self):
        s = "abcdefgh"
        c = "z"
        # For this case where the character "z" doesn't exist in the string,
        # the result should be a list of -1 for each index since the character does not appear.
        expected_result = [-1, -1, -1, -1, -1, -1, -1, -1]
        self.assertEqual(self.solution.shortestToChar(s, c), expected_result)

    def test_empty_string(self):
        s = ""
        c = "a"
        # In case of an empty string, the expected result is an empty list.
        expected_result = []
        self.assertEqual(self.solution.shortestToChar(s, c), expected_result)

if __name__ == '__main__':
    unittest.main()