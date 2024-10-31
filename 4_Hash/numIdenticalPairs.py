class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        hash_map = dict()
        count_good_pairs = 0

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                count_good_pairs += hash_map[num]
                hash_map[num] += 1
        return count_good_pairs

# nums = [1,2,3,1,1,3]
# nums = [1,1,1,1]
# nums = [1,2,3]
# t1 = Solution().numIdenticalPairs(nums)
# print(t1)

# Time Complexity: O(n)O(n)
# Space Complexity: O(n)O(n)