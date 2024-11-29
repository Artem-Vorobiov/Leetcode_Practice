class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        def invertion(value):
            return 1 - value  # Simplifies inversion: 0 becomes 1, and 1 becomes 0
        
        for subarray in image:
            left = 0
            right = len(subarray) - 1

            while left < right:
                # Flip the elements
                subarray[left], subarray[right] = subarray[right], subarray[left]
                # Invert both swapped elements
                subarray[left] = invertion(subarray[left])
                subarray[right] = invertion(subarray[right])
                left += 1
                right -= 1
            
            # Handle the middle element for odd-length rows
            if len(subarray) % 2 == 1:
                middle = len(subarray) // 2
                subarray[middle] = invertion(subarray[middle])

        return image


