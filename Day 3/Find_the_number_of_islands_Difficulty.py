class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1:
                return
            
            # Mark as visited
            grid[i][j] = '#'
            
            # Check all 8 directions
            directions = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)
            ]
            
            for di, dj in directions:
                dfs(i + di, j + dj)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    islands += 1
        
        return islands
