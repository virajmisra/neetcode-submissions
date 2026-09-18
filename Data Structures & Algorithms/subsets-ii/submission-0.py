class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []


        def dfs(curr, i):
            if i == len(nums):
                s = sorted(curr)
                if s not in res:
                    res.append(s.copy())
                return

            curr.append(nums[i])
            dfs(curr,i+1)
            curr.pop()
            dfs(curr,i+1)
        dfs([],0)
        return res
