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
                coord = str(i) + "," + str(j)
                grids[coord] = set()
        
        for r in range(9):
            for c in range(9):
                p = board[r][c]
                if p == ".":
                    continue
                
                coord = str(r//3) + "," + str(c//3)
                if p in rows[r] or p in cols[c] or p in grids[coord]:
                    return False
                rows[r].add(p)
                cols[c].add(p)
                grids[coord].add(p)
        return True
        