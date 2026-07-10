class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1

        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])

        for num in counts.keys():
            buckets[counts[num]].append(num)
        
        res = []
        i = len(buckets) - 1
        while i > 0 and len(res) < k:
            if buckets[i]:
                for num in buckets[i]:
                    if len(res) < k:
                        res.append(num)
            i -= 1
        return res
                    

