class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seen = set(nums)
        for num in seen:
            if num - 1 not in seen:
                curr = 1
                while num + 1 in seen:
                    curr = curr + 1
                    num = num + 1
                res = max(res,curr)
        return res
            