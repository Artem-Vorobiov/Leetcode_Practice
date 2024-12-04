print("")

class Solution:
    def intersction(self, nums1: list[int], nums2: list[int]) -> list[int]:

        # Function that create Count Dict
        def count_dict(word):
            mapping = {}
            for char in word:
                if char in mapping:
                    mapping[char] += 1
                else:
                    mapping[char] = 1
            return mapping
        
        mapping_word_1 = count_dict(nums1)
        mapping_word_2 = count_dict(nums2)
        print("Hashmap Created", mapping_word_1, mapping_word_2)

        # Main cycle. Iterating over the Keys of the Hashmap created from the shortest list
        # Look into the second hashmap if the Key is in there
        # if the Keys are present in both Hashmaps then we add to a new list of answers
        # BUT freuqencies could be differnt, so we need to  keep adding to a new list(mayve while loop) untill one of the freq is not 0
        def logic(map_short, map_long):
            result = []

            print("Start main logic")
            for key, value in map_short.items():
                print(map_short, "  ",map_long)
                if key in map_long:
                    while map_short[key] != 0 and map_long[key] != 0:
                        result.append(key)
                        map_short[key] -= 1
                        map_long[key] -= 1
            return result
 
        # Conditions for choosing the shortest array
        if len(nums1) <= len(nums2):
            print("First array is the shortest")
            res = logic(mapping_word_1, mapping_word_2)
        else:
            print("Second array is the shortest")
            res = logic(mapping_word_2, mapping_word_1)
        
        return res
    

