class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for n in nums:
            m[n] = m.get(n,0) + 1

        buckets = []
        # frequencies are [1, len(nums)]
        for i in range(len(nums) + 1):
            buckets.append([])
        
        for num in m:
            buckets[m[num]].append(num)
        
        i = len(buckets) - 1
        res = []
        while len(res) < k:
            while len(buckets[i]) > 0 and len(res) < k:
                res.append(buckets[i].pop())
            i = i - 1
        return res