class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])
        visitedPacific = set()
        visitedAtlantic = set()
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        res = []

        def dfs(r, c, visited, lastHeight):
            if((r,c) in visited or r < 0 or c < 0 or r == rows or c == columns or
                heights[r][c] < lastHeight):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])


        # Top and bottom row
        for c in range(columns):
            dfs(0, c, visitedPacific, heights[0][c])
            dfs(rows - 1, c, visitedAtlantic, heights[rows - 1][c])
        
        # Left and right col
        for r in range(rows):
            dfs(r, 0, visitedPacific, heights[r][0])
            dfs(r, columns - 1, visitedAtlantic, heights[r][columns - 1])

        for r in range(rows):
            for c in range(columns):
                if((r,c) in visitedPacific and (r,c) in visitedAtlantic):
                    res.append([r,c])
        
        return res

        