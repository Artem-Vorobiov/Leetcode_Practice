class Solution:
    def frequencySort(self, s: str) -> str:
        count_dict = {}
        
        for i in s:
            if i not in count_dict:
                count_dict[i] = 1
            else:
                count_dict[i] += 1
                
        sorted_dict = sorted(count_dict.items(), key = lambda x: x[1], reverse = True)
        new_word = []

        for i in sorted_dict:
            new_word.append(i[0]*i[1])

        return ''.join(new_word)


# Space Complexity: On + Ok log k + Ok = On log n
# Time Complexity: On + Om + Ok = On