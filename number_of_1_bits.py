class Solution(object):
    def hammingWeight(self, n):
        # converting to binary - removing zeros - and count 1 
        # b = list(bin(n)[2:].replace('0', ''))
        # count = b.count('1')
        # return count 
        
        # bit manipulation 
        count = 0 
        while n:
            count += n & 1
            n >>= 1
        return count 

