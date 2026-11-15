class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0;
        rows = len(grid)
        columns = len(grid[0])
        count = 0
        visited = set() 
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(row, col):
            q = collections.deque()
            visited.add((row, col))
            q.append((row, col))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    newRow = r + dr
                    newCol = c + dc
                    if(newRow in range(rows) and newCol in range(columns) and grid[newRow][newCol] == "1" and (newRow, newCol) not in visited):
                        q.append((newRow, newCol))
                        visited.add((newRow, newCol))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    count += 1

        return count

            
