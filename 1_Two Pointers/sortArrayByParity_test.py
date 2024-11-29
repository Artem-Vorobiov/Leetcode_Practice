import unittest
from sortArrayByParity import Solution

class sortArrayByParityTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        input = [3,1,2,4]
        output = [2,4,3,1]
        self.assertEqual(self.solution.sortArrayByParity(input), output)

    def test_case_2(self):
        input = [0]
        output = [0]
        self.assertEqual(self.solution.sortArrayByParity(input), output)

if __name__ == '__main__':
    unittest.main()