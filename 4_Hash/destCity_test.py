import unittest
from destCity import Solution

# Unit Test for Solution class
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
        expected_output = "Sao Paulo"
        self.assertEqual(self.solution.destCity(paths), expected_output)

    def test_case_2(self):
        paths = [["B", "C"], ["D", "B"], ["C", "A"]]
        expected_output = "A"
        self.assertEqual(self.solution.destCity(paths), expected_output)

    def test_case_3(self):
        paths = [["A", "Z"]]
        expected_output = "Z"
        self.assertEqual(self.solution.destCity(paths), expected_output)
    
    def test_empty_paths(self):
        paths = []
        expected_output = None
        self.assertEqual(self.solution.destCity(paths), expected_output)



if __name__ == '__main__':
    unittest.main()
