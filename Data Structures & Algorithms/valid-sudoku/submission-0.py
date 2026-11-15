class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr != ".":
                    row = f"{curr} in row {i}"
                    col = f"{curr} in col {j}"
                    box = f"{curr} in between {i//3} - {j//3}"
                    if row in seen or col in seen or box in seen:
                        return False
                    else:
                        seen.add(row)
                        seen.add(col)
                        seen.add(box)
        return True
