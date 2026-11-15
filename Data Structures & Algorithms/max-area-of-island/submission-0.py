class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        res = 0
        if not grid:
            return 0
        
        visited = set()

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            count = 1

            while(q):
                row, col = q.popleft()
                for a, b in directions:
                    newRow = row + a
                    newCol = col + b
                    if(newRow in range(ROWS) and newCol in range(COLUMNS) and (newRow,newCol) not in visited 
                        and grid[newRow][newCol] == 1):
                        q.append((newRow, newCol))
                        visited.add((newRow, newCol))
                        count += 1

            return count
        
        for r in range(ROWS):
            for c in range(COLUMNS):
                if (r,c) not in visited and grid[r][c] == 1:
                    area = bfs(r,c)
                    res = max(res, area)

        return res
                


