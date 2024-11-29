print("")
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:

        pointer_main = 0
        pointer_odd = 0
        length = len(nums)

        while pointer_main < length:
            # When first element is ODD:
            if nums[pointer_main] % 2 == 0 and pointer_main == 0:
                pass

            if nums[pointer_main] % 2 == 0:
                nums[pointer_odd], nums[pointer_main] = nums[pointer_main], nums[pointer_odd]
                pointer_odd += 1

            pointer_main += 1
        return nums
    

