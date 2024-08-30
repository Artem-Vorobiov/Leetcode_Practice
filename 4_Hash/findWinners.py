# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

#     answer[0] is a list of all players that have not lost any matches.
#     answer[1] is a list of all players that have lost exactly one match.

# The values in the two lists should be returned in increasing order.

# Note:

#     You should only consider the players that have played at least one match.
#     The testcases will be generated such that no two matches will have the same outcome.


class Solution:
    def findWinners(self, matches):
        unique_elements = set(item for sublist in matches for item in sublist)
        hash = {i: 0 for i in unique_elements}
        
        for pair in matches:
            if pair[1] in hash:
                hash[pair[1]] += 1

        ans_1 = [key for key, value in hash.items() if value == 0]
        ans_2 = [key for key, value in hash.items() if value == 1]

        return [sorted(ans_1), sorted(ans_2)]