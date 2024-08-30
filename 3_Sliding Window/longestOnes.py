class Solution:
    def longestOnes(self, nums, k):
        left = curr = ans = 0
        length = len(nums)

        for right in range(length):
            if nums[right] == 0:
                curr += 1
                while curr > k:
                    if nums[left] == 0:
                        curr -= 1
                    left += 1
            
            ans = max(ans,right - left + 1)
        return ans
                        