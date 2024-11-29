import unittest
from flipAndInvertImage import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        """Initialize Solution instance for all tests."""
        self.solution = Solution()

    def test_even_length_rows(self):
        """Test the function with a 2D image having even-length rows."""
        image = [[1, 0], [0, 1]]
        expected = [[1, 0], [0, 1]]  # Flip and invert returns the same in this case
        result = self.solution.flipAndInvertImage(image)
        self.assertEqual(result, expected)

    def test_odd_length_rows(self):
        """Test the function with a 2D image having odd-length rows."""
        image = [[1, 1, 0], [0, 0, 1]]
        expected = [[1, 0, 0], [0, 1, 1]]
        result = self.solution.flipAndInvertImage(image)
        self.assertEqual(result, expected)

    def test_single_row(self):
        """Test the function with a single row."""
        image = [[1, 0, 1]]
        expected = [[0, 1, 0]]
        result = self.solution.flipAndInvertImage(image)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
