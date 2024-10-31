class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        def convert_to_list(variable, is_pattern=False):
            # For pattern, split into individual characters
            if is_pattern:
                result = list(variable)
            else:
                # Split the string into words based on spaces
                result = variable.split()
            return result

        def make_alphabet(element, is_pattern=False):
            el_list = convert_to_list(element, is_pattern)
            alphabet = {}

            for index, el in enumerate(el_list):
                if el not in alphabet:
                    alphabet[el] = index
            return el_list, alphabet
        
        # Treat pattern as characters, and s as words
        el_list_1, alphabet_1 = make_alphabet(pattern, is_pattern=True)
        el_list_2, alphabet_2 = make_alphabet(s, is_pattern=False)

        # Check if the lengths of distinct elements match
        if len(el_list_1) != len(el_list_2):
            return False

        # Map the elements to their indices
        mapped_list_1 = [alphabet_1[el] for el in el_list_1]
        print(f'Element list: {el_list_1}, alphabet: {alphabet_1}, Map: {mapped_list_1}')

        mapped_list_2 = [alphabet_2[el] for el in el_list_2]

        # Compare the mapped lists
        return mapped_list_1 == mapped_list_2

# Example usage
solution = Solution()
print(solution.wordPattern("abba", "dog cat cat dog"))  # Output: True
print(solution.wordPattern("abba", "dog cat cat fish"))  # Output: False
print(solution.wordPattern("e", "eukera"))  # Output: True
