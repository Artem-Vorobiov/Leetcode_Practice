class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        s = list(s)
        storage = dict()
        res = left = 0

        for index, right in enumerate(s):
            while right in storage:
                del storage[s[left]]
                left += 1
            if right not in storage:
                storage[right] = 0
            res = max(res, index-left+1)
        
        return res

#       Time Complexity
# Time complexity: O(n), where n is the length of the string s. 
# This is because both the left and right pointers only traverse the string linearly.

#       Space Complexity
#  O(k), where k is the number of unique characters in s. In the worst case, this is O(n) if all characters are unique.
