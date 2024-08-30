# Given an array of integers nums, you start with an initial positive value startValue.

# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

# Return the minimum positive value of startValue such that the step by step sum is never less than 1.


class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        startValue = 1
        while True:
            prefix = [startValue]
            for i in range(1, (len(nums)+1)):
                if (prefix[i-1]+nums[i-1]) < 1:
                    break
                else:
                    prefix.append(prefix[i-1]+nums[i-1])

            if (len(nums)+1) == len(prefix):
                return startValue
 
            startValue += 1