class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k
# nums = [0,0,1,1,1,2,2,3,3,4]

# nums = [2]
# val = 3

# nums = [3,2,2,3]
# val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2

w1 = Solution().removeElement(nums, val)
print(w1)

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
        
#         if len(haystack) < len(needle):
#             return -1
        
#         for i in range(len(haystack)):
#             if needle == haystack[i : i + len(needle)]:
#                 return i
            
#         return -1


# # haystack = "sadbutsad"
# # needle = "sad"

# haystack = "leetcode"
# needle = "leeto"
# w1 = Solution().strStr(haystack, needle)
# print(w1)