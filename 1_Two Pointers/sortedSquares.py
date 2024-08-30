# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.


class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)