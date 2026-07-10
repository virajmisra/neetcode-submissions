class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c,pos):
            if pos == len(word):
                return True
            if (r == rows or
            c == cols or 
            c == -1 or 
            r == -1 or
            word[pos] != board[r][c]):
                return False

            pos+=1
            t = board[r][c]
            board[r][c] = "#"

            res = (dfs(r+1,c,pos) or
            dfs(r,c+1,pos) or
            dfs(r-1,c,pos) or
            dfs(r,c-1,pos))

            board[r][c] = t
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False


        