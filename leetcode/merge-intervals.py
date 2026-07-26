class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key = lambda x: x[0])

        res = [intervals[0]]

        for s,e in intervals[1:]:
            
            start,end = res[-1][0], res[-1][1]
            
            if s <= end: # can merge
                res[-1] = [start, max(e, end)]
            else:
                res.append([s,e])
        
        return res