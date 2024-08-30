
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

class Solution:
    def findMaxLength(self, nums):
            hash = {}
            curr = ans = 0

            for i, num in enumerate(nums):
                if num == 0:
                    curr -= 1
                else:
                    curr += 1

                if curr == 0:
                    ans = i + 1
                elif curr in hash:
                    ans = max(ans, i - hash[curr])
                else:
                    hash[curr] = i

            return ans

    

        