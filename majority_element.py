class Solution(object):
    def majorityElement(self, nums):
        count = 0 
        candidate = 0 

        for i in nums:
            if count == 0 :
                candidate = i 
            if i == candidate :
                count += 1 
            else : 
                count -= 1
        
        if nums.count(candidate) > len(nums) // 2 :
            return candidate 
        