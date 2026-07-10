class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)
        res = 0
        for n in nums:
            num = n
            count = 1
            while (num+1) in s:
                count+=1
                num+=1
            res = max(count,res)
        return res
        