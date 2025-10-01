class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1 
        x2 = str(abs(x))
        x2 = x2[::-1]

        x2 = int(x2) * sign
        if x2 < -2**31 or x2 > 2**31-1:
            return 0 
        return x2