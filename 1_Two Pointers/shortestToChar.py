class Solution():

    # Custom function to find the first occurance of CHAR on the left side 
    # def custom_left_find(self, s: str, c: str) -> int:
    def custom_right_find(self, s: str, c: str) -> int:
        for i in range(len(s)):
            if s[i] == c:
                return i 
        return -1

    # Custom function to find the first occurence if CHAR on the right side
    # def custom_right_find(self, s: str, c: str) -> int:
    def custom_left_find(self, s: str, c: str) -> int:
        for i in range((len(s)-1), -1, -1):
            if s[i] == c:
                return i
        return -1

    def shortestToChar(self, s: str, c: str) -> list[int]:
        answers = []
        n = len(s)
        char_left = None
        char_right = None

        for i in range(n):
            if c in s[:i]:
                char_left = self.custom_left_find(s[:i], c)
            if c in s[i:]:
                char_right = self.custom_right_find(s[i:],c) + i 

            if char_left is not None and char_right is not None:
                value_left = abs(i-char_left)
                value_right = abs(i-char_right)
                answers.append(min(value_left,value_right))
            elif char_left is not None:
                value_left = abs(i-char_left)
                answers.append(value_left)
            elif char_right is not None:
                value_right = abs(i-char_right)
                answers.append(value_right)
        
        return answers

s = "loveleetcode"
c = "e"
sol = Solution()  # Create an instance of the Solution class
t1 = sol.shortestToChar(s, c)  # Call the method with the test string and character


# Space Complexity O(n)
# Time complexity O(n)