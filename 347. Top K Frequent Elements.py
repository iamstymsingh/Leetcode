import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = dict()
        for num in nums:
            freq_counter[num] = freq_counter.get(num, 0) + 1

        min_heap = []
        for num, freq in freq_counter.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        output = []
        while min_heap:
            freq, num = heapq.heappop(min_heap)
            output.append(num)
        return output[::-1]
