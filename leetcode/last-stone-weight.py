class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            if x != y:
                newWeight = abs(y - x)
                heapq.heappush(maxHeap, newWeight * -1)
                
        if len(maxHeap) == 1:
            return maxHeap[0] * (-1)
        return 0