import unittest
from isPathCrossing_1 import Solution  # Replace 'your_solution_file' with the actual file name

class TestIsPathCrossing(unittest.TestCase):
    
    def test_path_does_not_cross(self):
        path = "NES"
        solution = Solution()
        self.assertFalse(solution.isPathCrossing(path), "Expected False since path does not cross")
    
    def test_path_crosses(self):
        path = "NESWW"
        solution = Solution()
        self.assertTrue(solution.isPathCrossing(path), "Expected True since path crosses")

if __name__ == "__main__":
    unittest.main()
