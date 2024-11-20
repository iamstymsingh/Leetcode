import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        distances = self.calcDistance(points)
        for idx, distance in enumerate(distances):
            heapq.heappush(max_heap, (-distance, points[idx]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        output = []
        while len(max_heap) > 0:
            vals = heapq.heappop(max_heap)
            output.append(vals[1])
        return output

    def calcDistance(self, points: List[List[int]]) -> List[int]:
        distances = []
        for point in points:
            distance = math.sqrt(point[0]**2 + (point[1]**2))
            distances.append(distance)
        return distances