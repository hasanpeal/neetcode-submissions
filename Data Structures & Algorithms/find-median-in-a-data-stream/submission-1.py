class MedianFinder:

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        if self.maxHeap and num > self.maxHeap[0]:
            heapq.heappush(self.maxHeap, num)
        else:
            heapq.heappush(self.minHeap, -1 * num)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap) * -1
            heapq.heappush(self.maxHeap, val)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -1 * val)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0] * -1
        return ((-1 * self.minHeap[0]) + self.maxHeap[0]) / 2.0
        
        