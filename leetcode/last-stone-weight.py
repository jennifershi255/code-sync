class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap) # heaviest
            x = -heapq.heappop(heap) # second heaviest

            if x != y:
                heapq.heappush(heap, x-y)
        
        if heap:
            return -heap[0]
        else:
            return 0