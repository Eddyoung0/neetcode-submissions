import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counterS = Counter(nums)
        heap = []

        for val, key in counterS.items():
            if len(heap) < k:
                heapq.heappush(heap, (key, val))
            else:
                heapq.heappushpop(heap, (key, val))
        return [h[1] for h in heap]