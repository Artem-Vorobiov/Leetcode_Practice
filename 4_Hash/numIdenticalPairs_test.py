import unittest
from numIdenticalPairs import Solution

class numIdenticalPairsTEST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_case_1(self):
        input = [1,2,3,1,1,3]
        expected = 4
        self.assertEqual(self.solution.numIdenticalPairs(input), expected)

    def test_case_2(self):
        input = [1,1,1,1]
        expected = 6
        self.assertEqual(self.solution.numIdenticalPairs(input), expected)

    def test_case_3(self):
        input = [1,2,3]
        expected = 0 
        self.assertEqual(self.solution.numIdenticalPairs(input), expected)

if __name__ == '__main__':
    unittest.main()