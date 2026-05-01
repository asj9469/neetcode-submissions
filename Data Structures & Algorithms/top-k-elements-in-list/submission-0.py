from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first get the frequency of each number
        # trick: always keep k elements in the heap to make things a bit more constant

        freq = defaultdict(int)
        heap = []

        for n in nums:
            freq[n] += 1
        
        for key, val in freq.items():
            heapq.heappush(heap, (val, key))

            if len(heap) > k:
                heapq.heappop(heap)

        return [node[1] for node in heap]

        