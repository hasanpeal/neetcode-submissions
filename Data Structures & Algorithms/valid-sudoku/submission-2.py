class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr != ".":
                    row = f"{curr} in row {i}"
                    col = f"{curr} in col {j}"
                    box = f"{curr} in board{(i//3)*3 + j//3}"
                    if box in seen or row in seen or col in seen:
                        return False
                    else:
                        seen.add(row)
                        seen.add(col)
                        seen.add(box)
        
        return True