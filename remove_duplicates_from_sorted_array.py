class Solution(object):
    def removeDuplicates(self, nums):
        nums.sort()
        new_nums = [] 

        for i in nums:
            if i not in new_nums:
                new_nums.append(i)

        nums[:] = new_nums 

        return len(nums)
