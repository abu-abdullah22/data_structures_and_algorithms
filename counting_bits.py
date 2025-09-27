class solution(object):
    def countBits(self,n):
        ans = []
        
        for i in range(n+1):
            binary_string = bin(i)[2:]
            count = binary_string.count('1')
            ans.append(count)
            
        return ans 