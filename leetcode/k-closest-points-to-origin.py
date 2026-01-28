class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distance = []

        for p in points:
            d = -(((p[0] - 0)**2 + (p[1] - 0)**2)**(1/2))
            heapq.heappush(distance, [d,p])
            if len(distance) > k:
                heapq.heappop(distance)


        points = []
        while distance:
            points.append(heapq.heappop(distance)[1])
        
        return points