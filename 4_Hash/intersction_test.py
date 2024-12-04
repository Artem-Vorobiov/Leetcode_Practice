from intersction import Solution
import unittest

class TestIntersection(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        expected_output = [2, 2]  # Order doesn't matter
        result = self.solution.intersction(nums1, nums2)
        self.assertCountEqual(result, expected_output, "Test case 1 failed")

    def test_case_2(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        expected_output = [4, 9]  # Order doesn't matter
        result = self.solution.intersction(nums1, nums2)
        self.assertCountEqual(result, expected_output, "Test case 2 failed")

    def test_case_3(self):
        nums1 = []
        nums2 = [1, 2, 3]
        expected_output = []  # No intersection
        result = self.solution.intersction(nums1, nums2)
        self.assertEqual(result, expected_output, "Test case 3 failed")

if __name__ == "__main__":
    unittest.main()
