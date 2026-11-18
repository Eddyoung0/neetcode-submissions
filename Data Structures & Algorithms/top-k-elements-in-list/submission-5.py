class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counterS = Counter(nums)
        heap =[]
        for key, val in counterS.items():
            if len(heap) < k:
                heapq.heappush(heap,(val, key))
            else:
                heapq.heappushpop(heap,(val, key))
        return [h[1] for h in heap]