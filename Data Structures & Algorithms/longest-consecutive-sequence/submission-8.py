class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # only want to consider numbers where
        # its the first of the sequence
        s = set(nums)
        res = 0
        for n in nums:
            if n-1 not in s:
                streak = 1
                while n+1 in s:
                    n = n + 1
                    streak = streak + 1
                res = max(streak,res)
        return res
        