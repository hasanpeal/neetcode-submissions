class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        heap = []
        res = []

        for n in nums:
            count[n] += 1
        
        # Iterate over keys and push tupe (freq, num) to min heap
        for key in count.keys():
            heapq.heappush(heap, (count[key], key))
            if len(heap) > k: # Keep only bottom 2 item of heap (max)
                heapq.heappop(heap)
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1]) # Keep poping and add to res

        return res