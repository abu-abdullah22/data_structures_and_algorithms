class Solution(object):
    def productExceptSelf(self, nums):
       zero_count = nums.count(0)
       product = 1
       final_arr = []

       if zero_count > 1 :
        final_arr = [0] * len(nums)
        
       elif zero_count == 1:
        for i in nums:
            if i != 0:
                product *= i

        for j in range(len(nums)):
            if nums[j] == 0:
                final_arr.append(product)
            else:
                final_arr.append(0)

       else:
        for i in nums:
            product *= i 

        for j in range(len(nums)):
            final_arr.append(product // nums[j])
        
       return final_arr