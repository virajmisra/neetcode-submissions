class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c,i):
            if i == len(word):
                return True
            elif r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            
            i += 1
            t = board[r][c]
            board[r][c] = "#"
            res = dfs(r+1,c,i) or dfs(r,c+1,i) or dfs(r-1,c,i) or dfs(r,c-1,i)

            board[r][c] = t
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False

        