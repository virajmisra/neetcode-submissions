class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(pos,curNums,curSum):
            if curSum == target:
                res.append(curNums.copy())
                return
            if pos >= len(nums) or curSum > target:
                return
            curNums.append(nums[pos])
            dfs(pos,curNums,curSum+nums[pos])
            curNums.pop()
            dfs(pos+1,curNums,curSum)
        dfs(0,[],0)
        return res