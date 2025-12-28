class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        prev = [1]

        while (rowIndex > 0):
            curr = []
            curr.append(1)
            l = 0
            r = 1
            for i in range(1, len(prev)):
                curr.append(prev[l] + prev[r])
                l += 1
                r += 1
                
            curr.append(1)
            prev = curr
            rowIndex -= 1
        
        return prev