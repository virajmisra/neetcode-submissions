class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        #[1, 2, 2, 4, 5, 6, 9]
        def dfs(i,curr,total):
            if total == target:
                res.append(curr.copy())
                return
            elif total > target or i > len(candidates)-1:
                return
            
            curr.append(candidates[i])
            dfs(i+1,curr,total + candidates[i])

            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1,curr,total)
        dfs(0,[],0)
        return res

        