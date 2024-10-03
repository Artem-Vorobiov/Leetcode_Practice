class Solution():
    def fixedWindow(self, nums: list[int], k: int) -> int:
        curr = ans = 0 

        # Exceptions
        if len(nums) < k:
            print("\nLength of the array is shorter than constrain\n")
            return False
        elif k == 0:
            print("\nConstrain should be greater than 0\n")
            return False

        # Main Cycle
        for right in range(len(nums)):
            left = right - k + 1

            if left < 0:
                continue
            else:
                ans_1 = sum(nums[left:(right+1)])
            
            ans = max(ans, ans_1)

        return ans


# Pay attention to this IDEA. If you write sum(nums[0:1]) you would not get the sum of the first and second element.
# If you write sum(nums[0:2]), you would get expected SUM.
# You can stuck with this.


