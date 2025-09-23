class Solution(object):
    def firstMissingPositive(self, nums):

        positive_nums = set([num for num in nums if num > 0 ])

        i = 1 

        while True:
            if i not in positive_nums:
                return i 
            i += 1 