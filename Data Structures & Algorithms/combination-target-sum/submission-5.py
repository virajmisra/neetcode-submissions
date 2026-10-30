class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.res = []
        def dfs(curr, i, total):
            if total > target or i > len(nums) - 1:
                return
            elif total == target:
                self.res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(curr,i,total+nums[i])
            curr.pop()
            dfs(curr,i+1,total)
        dfs([],0,0)
        return self.res