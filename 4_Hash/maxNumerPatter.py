# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
class Solution:
    def maxNumberOfBalloons(self, text, pattern):
        
        # Initialize hashmaps (dictionaries) for frequencies
        freqInText = {}
        freqInPattern = {}
        
        # Calculate the frequency of each character in text
        for char in text:
            if char in freqInText:
                freqInText[char] += 1
            else:
                freqInText[char] = 1
        
        # Calculate the frequency of each character in pattern
        for char in pattern:
            if char in freqInPattern:
                freqInPattern[char] += 1
            else:
                freqInPattern[char] = 1
        
        # Compare the maximum string that can be produced
        answer = float('inf')
        for char in freqInPattern:
            if char in freqInText:
                answer = min(answer, freqInText[char] // freqInPattern[char])
            else:
                # If a character in the pattern is missing from the text, return 0
                return 0
        
        return answer