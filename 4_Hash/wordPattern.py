class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        def convert_to_list(variable):
            # Check if there's a space in the input string
            if ' ' in variable:
                # Check if the string ends with a space
                if not variable.endswith(' '):
                    raise ValueError("Each word must be followed by a space.")
                
                # Split the string into a list of words
                result = variable.split()
            else:
                # If no space, convert the string into a list of characters
                result = list(variable)
            
            return result

        def make_alphabet(element):
            el_list = convert_to_list(element)
            alphabet = {}

            for index, el in enumerate(el_list):
                if el not in alphabet:
                    alphabet[el] = index
            return el_list, alphabet
        
        el_list_1, alphabet_1 = make_alphabet(pattern)
        el_list_2, alphabet_2 = make_alphabet(s)

        # Check if the lengths of distinct elements match
        if len(alphabet_1) != len(alphabet_2):
            return False

        # Map the elements to their indices
        mapped_list_1 = [alphabet_1[el] for el in el_list_1]
        mapped_list_2 = [alphabet_2[el] for el in el_list_2]

        # Compare the mapped lists
        return mapped_list_1 == mapped_list_2

# Example usage
solution = Solution()
print(solution.wordPattern("abba", "dog cat cat dog "))  # Output: True
print(solution.wordPattern("abba", "dog cat cat fish "))  # Output: False
