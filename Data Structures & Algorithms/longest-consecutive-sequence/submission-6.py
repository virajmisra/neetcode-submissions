class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:   
        s = set(nums)
        res = 0
        for n in nums:
            streak = 0
            if n - 1 not in s:
                streak += 1
                while n + streak in s:
                    streak += 1
            res = max(res,streak)
        return res
            
        