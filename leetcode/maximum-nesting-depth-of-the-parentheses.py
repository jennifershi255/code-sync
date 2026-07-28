class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        curr = 0

        for c in s:
            if c == "(":
                curr += 1
                res = max(res, curr)
                continue
            
            if c == ")":
                curr -= 1
            
        
        return res