class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # You need to make sure that length is the same
        # You need to make sure that key's are the same
        # You need to make sure that frequencies are the same
        # You cannot SUM the frequencies because the frequencies distribution(or patter) is important!

        # Check Length +++
        if len(word1) != len(word2):
            return False

        def count_dict(word):
            mapping = {}
            for char in word:
                if char in mapping:
                    mapping[char] += 1
                else:
                    mapping[char] = 1
            return mapping
        
        # Create count dict
        word_1_dict = count_dict(word1)
        word_2_dict = count_dict(word2)

        # Set for checking letters
        letter_word_1 = set(word_1_dict.keys())
        letter_word_2 = set(word_2_dict.keys())

        # list of Values
        values_1_dict = sorted(list(word_1_dict.values()))
        values_2_dict = sorted(list(word_2_dict.values()))

        return letter_word_1 == letter_word_2 and values_1_dict == values_2_dict




        
