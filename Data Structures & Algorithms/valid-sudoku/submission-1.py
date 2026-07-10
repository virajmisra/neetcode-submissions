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
                coord = str(i) + str(j)
                grids[coord] = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr != '.':
                    coord = str(i//3) + str(j//3)
                    if curr in rows.get(i) or curr in cols.get(j) or curr in grids.get(coord):
                        return False
                    
                    rows[i].add(curr)
                    cols[j].add(curr)
                    grids[coord].add(curr)
        return True
                    
                

