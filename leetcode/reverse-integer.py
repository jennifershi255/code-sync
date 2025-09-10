class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        res = ""
        isNeg = True

        if x < 0:
            isNeg = True
        else:
            isNeg = False

        x = abs(x)
        while x != 0:
            res += str(x % 10)
            x = x // 10
        
        if res:
            res = int(res)
        
        if res >= -(2**31) and res <= (2**31 - 1):
            if isNeg:
                return res * -1
            else:
                return res
        
        return 0