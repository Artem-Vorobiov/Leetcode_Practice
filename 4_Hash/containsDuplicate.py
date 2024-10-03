class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        original_length = len(nums)
        checked_length = len(set(nums))

        if original_length == checked_length:
            return False
        else:
            return True
        
if __name__ == '__main__':
    sol = Solution()

    test_nums = [1, 2, 3, 4]  # No duplicates
    print(f"\nDoes {test_nums} contain duplicates? {sol.containsDuplicate(test_nums)}\n")
