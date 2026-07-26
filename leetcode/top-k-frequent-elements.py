class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = Counter(nums)

        minHeap = []
        
        for num, f in freq.items():
            heapq.heappush(minHeap, (f, num))

            if len(minHeap) > k:
                heapq.heappop(minHeap) # pops the smallest
        
        return [num for f, num in minHeap]