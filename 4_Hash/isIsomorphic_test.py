import unittest
from isIsomorphic import Solution

class TestisIsomorphic(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        input = ['egg', 'add']
        expected = True
        self.assertEqual(self.solution.isIsomorphic(input[0], input[1]), expected)

    def test_case_2(self):
        input = ['paper', 'title']
        expected = True
        self.assertEqual(self.solution.isIsomorphic(input[0], input[1]), expected)

    def test_case_3(self):
        input = ['paper', 'titsdfsle']
        expected = False
        self.assertEqual(self.solution.isIsomorphic(input[0], input[1]), expected)


if __name__ == '__main__':
    unittest.main()