# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

# reversePrefix.py

class Solution:
    def reversePrefix(self, word, ch):
        lower_word = word.lower()
        ch = ch.lower()

        if ch in lower_word:
            arr = list(word)
            div = lower_word.index(ch)
            right = div + 1
            left_arr = arr[:right]
            right_arr = arr[right:]

            # Reverse the left_arr in place
            left_arr = left_arr[::-1]

            finale = ''.join(left_arr + right_arr)
            return finale
        else:
            return word  # Return the original word if 'ch' is not found

