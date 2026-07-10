class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        grids = {}

        for i in range(9):
            rows[i] = set()
            cols[i] = set()
        
        for i in range(3):
            for j in range(3):
                grids[i,j] = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                coord = (r//3,c//3)
                n = board[r][c]
                if n == ".":
                    continue
                if (n in rows[r] or
                n in cols[c] or
                n in grids[coord]):
                    return False
                rows[r].add(n)
                cols[c].add(n)
                grids[coord].add(n)
        return True
