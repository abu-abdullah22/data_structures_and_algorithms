class Solution(object):
    def reverseWords(self, s):
        t = [s][0].split()

        t.reverse()

        return ' '.join(t)
        