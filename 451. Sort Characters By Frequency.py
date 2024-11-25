from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        heap = []
        for k, v in counter.items():
            heapq.heappush(heap, (-v, k))

        output = ""
        while heap:
            popped = heapq.heappop(heap)
            value = popped[1] * abs(popped[0]) 
            output += value
        return output
