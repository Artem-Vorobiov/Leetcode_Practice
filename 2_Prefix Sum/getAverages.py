# You are given a 0-indexed array nums of n integers, and an integer k.

# The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

# The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.


class Solution:
    def getAverages(self, nums, k):
        if k == 0:
            return nums
        
        averages = [-1] * len(nums)

        window_size = k*2 + 1
        if window_size > len(nums):
            return averages
        
        window_sum = sum(nums[:window_size])
        averages[k] = window_sum // window_size

        for i in range(window_size, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - window_size]
            averages[i-k] = window_sum // window_size
        return averages