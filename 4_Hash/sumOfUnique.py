class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        
        alphabet = {}
        max_value = ans = 0

        for index, el in enumerate(nums):
            if el not in alphabet:
                alphabet[el] = 1
            else:
                alphabet[el] += 1
            max_value = max(max_value, alphabet[el])

        for key, value in alphabet.items():
            if value == max_value:
                ans += value
        
        return ans 

# nums = [1,2,2,3,1,4]
nums = [1,2,3,4,5]    
w1 = Solution().maxFrequencyElements(nums)
