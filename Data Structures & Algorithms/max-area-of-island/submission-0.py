class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if (r < 0 or
            c < 0 or
            r >= rows or
            c >= cols or
            (r,c) in visited or
            grid[r][c] == 0):
                return 0
            area = 1
            visited.add((r,c))
            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c+1)
            area += dfs(r,c-1)
            return area

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    res = max(res,dfs(r,c))
        return res
