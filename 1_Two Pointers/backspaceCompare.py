class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def new_string(string: str) -> str:
            new_string = []

            for char in string:
                if char == "#":
                    if new_string: 
                        new_string.pop()
                else:
                    new_string.append(char)
            return ''.join(new_string)

        new_string_1 = new_string(s)
        new_string_2 = new_string(t)

        return new_string_1 == new_string_2
        

# Time Complexity   - O(n+m)
# Space complexity  - O(n+m)

# If n and m are independent and could vary significantly (e.g., n≫mn≫m or m≫nm≫n),
#   you cannot simplify O(n+m)O(n+m) to O(n)O(n) without losing precision. O(n+m)O(n+m) 
#   reflects the combined contributions of both variables.