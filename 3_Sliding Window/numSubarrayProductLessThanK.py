class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        left = ans = 0
        curr = 1

        if k <= 1:
            return 0

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr = curr // nums[left]
                left += 1

            ans += right - left + 1
        return ans
     
# Time complexity: O(n) - each element of FOR and WHILE loeps are visited once.
# Space complexity: O(1) -  the space used doesn't grow with the input size.