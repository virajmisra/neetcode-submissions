class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n,0) + 1

        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        
        for n in counts:
            freq = counts[n]
            buckets[freq].append(n)
        
        res = []
        for i in range(len(buckets)-1,-1,-1):
            while len(res) < k and len(buckets[i]) > 0:
                res.append(buckets[i].pop())
        return res