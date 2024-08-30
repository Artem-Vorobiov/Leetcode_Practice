# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = []
        j = 0
        for i in range(len(nums)):
            sum = nums[i]+j
            runningSum.append(sum)
            j = sum
        print(runningSum)
        return runningSum