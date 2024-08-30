# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1

        return res if res != float('inf') else 0
        