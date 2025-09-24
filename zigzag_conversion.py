class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        # rows = [[] for _ in range(numRows)]

        currentRow = 0 
        direction = 1

        for c in s :
            rows[currentRow] += c
            # rows[currentRow].append(c) 
            currentRow += direction 
            
            if currentRow == numRows - 1:
                direction = -1
            elif currentRow == 0 :
                direction = 1

        # return ''.join([''.join(row) for row in rows])  
        return ''.join(rows)