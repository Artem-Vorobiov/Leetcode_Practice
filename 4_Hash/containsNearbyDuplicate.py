class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}

        for i, val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            else:
                seen[val] = i
        return False

nums = [1,2,3,1]
k = 3
t1 = Solution().containsNearbyDuplicate(nums, k)
print(t1)

# Time complexity - O(n)
# Space Complexity - O(n)