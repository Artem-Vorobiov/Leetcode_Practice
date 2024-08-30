import unittest
from findWinners import Solution  # Replace 'your_solution_file' with the actual filename without '.py'
class TestFindWinners(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        matches = [[1, 2], [2, 3], [4, 5], [5, 6]]
        expected = [[1, 4], [2, 3, 5, 6]]  # Players 1 and 4 have not lost any matches; players 2, 3, 5, and 6 have lost exactly one match
        self.assertEqual(self.solution.findWinners(matches), expected)

    def test_case_2(self):
        matches = [[1, 2], [2, 3], [3, 4], [4, 1]]
        expected = [[], [1, 2, 3, 4]]  # All players have lost exactly one match
        self.assertEqual(self.solution.findWinners(matches), expected)

    def test_case_3(self):
        matches = [[1, 2], [3, 4], [5, 6]]
        expected = [[1, 3, 5], [2, 4, 6]]  # Players 1, 3, and 5 have not lost any matches; players 2, 4, and 6 have lost exactly one match
        self.assertEqual(self.solution.findWinners(matches), expected)

if __name__ == '__main__':
    unittest.main()
