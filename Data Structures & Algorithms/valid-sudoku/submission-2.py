class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        for i in range(9):
            rows[i] = set()
            cols[i] = set()
        
        grids = {}
        for i in range(3):
            for j in range(3):
                coord = str(i) + ", " + str(j)
                grids[coord] = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                elem = board[i][j]
                if elem == ".":
                    continue
                
                coord = str(i//3) + ", " + str(j//3)
                if elem in rows[i] or elem in cols[j] or elem in grids[coord]:
                    return False
                
                rows[i].add(elem)
                cols[j].add(elem)
                grids[coord].add(elem)
        return True
        