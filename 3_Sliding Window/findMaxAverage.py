# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums, k):
        best = now = sum(nums[:k])
        for i in range(k, len(nums)):
            now += nums[i] - nums[i - k]
            if now > best:
                best = now
        return float(best / k)
