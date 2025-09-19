class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(c for c in s if c.isalnum()).lower()
        t = list(s)
        t.reverse() 

        return t == list(s)
        