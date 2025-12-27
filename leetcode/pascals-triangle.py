class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1]]
        row = 0
        prev = res
        while (numRows > 1):
            new = [1]
            posL = 0
            posR = 1
            while (posR < len(res[row])):
                new.append(prev[posL] + prev[posR])    
                posL += 1
                posR += 1 
            new.append(1)
            numRows -= 1
            row += 1
            res.append(new)
            prev = new
        
        return res