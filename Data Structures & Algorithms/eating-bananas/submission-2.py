class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2

            time = 0
            for p in piles:
                time += math.ceil(p / m)
            
            if time <= h:
                # we can take more time, choose a slower rate
                r = m - 1
                res = m
            else:
                l = m + 1
        return res
        