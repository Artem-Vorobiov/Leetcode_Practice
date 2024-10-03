class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def convert_string_to_indices(string: str) -> list:
            alphabet = dict()
            morse = list()

            for index, char in enumerate(string):
                if char not in alphabet:
                    alphabet[char] = index
                    morse.append(index)
                else:
                    morse.append(alphabet[char])
            return morse

        word_1 = convert_string_to_indices(s)
        word_2 = convert_string_to_indices(t)

        if word_1 == word_2:
            return True
        else:
            return False
 

# w1 = Solution().isIsomorphic('egg', 'add')
# w2 = Solution().isIsomorphic('paper', 'title')
# w3 = Solution().isIsomorphic('paper', 'titsdfsle')

# Time Complexity - O(n) + O(n) + O(n) = O(n).
# Space Complexity - O(n) + O(n) = O(n).

