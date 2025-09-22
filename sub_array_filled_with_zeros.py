class Solution(object):
    def zeroFilledSubarray(self, nums):
        count = 0
        ans = 0
        for x in nums:
            if x == 0:
                count += 1
                ans += count 
            else:
                count = 0 
            
        return ans 
        

        # block_of_counts = []
        # current_count = 0

        # for x in nums:
        #     if x == 0 :
        #         current_count += 1
        #     else :
        #         block_of_counts.append(current_count)
        #         current_count = 0

        # if current_count > 0 :
        #     block_of_counts.append(current_count)
        
        # sum = 0

        # for y in block_of_counts:
        #     sum += y * (y + 1) // 2 

        

        # return sum 