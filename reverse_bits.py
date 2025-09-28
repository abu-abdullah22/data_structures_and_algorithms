class Solution(object):
    def reverseBits(self, n):
       n = format(n, '032b')
       reversed_n = n[::-1]

       return int(reversed_n, 2)
        