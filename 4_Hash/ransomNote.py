

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Quick check
        if len(magazine) < len(ransomNote): 
            return False 

        # Create alphabet
        alphabet = dict()
        for char in magazine.lower():
            if char in alphabet:
                alphabet[char] += 1
            else:
                alphabet[char] = 1

        # Final move. Can we make a word?
        for char in ransomNote.lower():
            if char in alphabet:
                if alphabet[char] != 0:
                    alphabet[char] -= 1
                else:
                    return False
            else:
                return False

        return True
    
#       Time Complexity
# O(m + n), where m is the length of magazine and n is the length of ransomNote.

#       Space Complexity
# O(k), where k is the number of unique characters in the magazine.