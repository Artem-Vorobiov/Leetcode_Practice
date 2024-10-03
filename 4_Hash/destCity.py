class Solution:
    def destCity(self, paths : list[list[str]]) -> str:

        if not paths:
            return None  # Handle empty paths case

        def make_alphabet(path_element, point):
            alphabet = dict()
            for el in path_element:
                if el[point] in alphabet:
                    alphabet[el[point]] += 1
                else:
                    alphabet[el[point]] = 0
            return alphabet
        
        alph_1 = make_alphabet(paths, 0)
        alph_2 = make_alphabet(paths, 1)

        for key in alph_2:
            if key not in alph_1:
                return key


# Time Complexity   - O(n) = O(n) + O(n) O(1)   - Linear
# Space Complexity  - O(n) = O(n) + O(n)        - Linear
# 