import unittest
from frequencySort import Solution

class frequencySortTEST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_case_1(self):
        input = 'tree'
        possible_outputs = ['eert', 'eetr']
        result = self.solution.frequencySort(input)
        self.assertIn(result, possible_outputs)

    def test_case_2(self):
        input = 'Aabb'
        possible_outputs = ['bbAa', 'bbaA']
        result = self.solution.frequencySort(input)
        self.assertIn(result, possible_outputs)

if __name__ == '__main__':
    unittest.main()