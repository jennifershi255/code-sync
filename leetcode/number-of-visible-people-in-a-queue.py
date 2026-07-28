class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        
        stack = []
        res = [0] * len(heights)

        for i in range(len(heights) - 1, -1, -1):
            count = 0

            while stack and stack[-1] < heights[i]:
                stack.pop() # remove the people shorter
                count += 1

            if stack: # we have a new maximum
                count += 1
            
            res[i] = count
            stack.append(heights[i]) 
        
        return res