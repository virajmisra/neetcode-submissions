class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            largest = heapq.heappop(heap)
            nLargest = heapq.heappop(heap)
            if largest != nLargest:
                heapq.heappush(heap,(largest-nLargest))
        return -heap[0] if heap else 0
            
        