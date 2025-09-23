class Solution(object):
    def increasingTriplet(self, nums):
        first = float('inf')
        second = float('inf')

        for i in nums:
            if i <= first :
                first = i 
                count = 1
            elif i <= second:
                second = i
                count = 2
            else:
                count = 3
                return True 
        
        return count >= 3