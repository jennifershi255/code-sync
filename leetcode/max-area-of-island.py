class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def dfs(r,c):
            if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == 1:
                grid[r][c] = 0
                return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            else:
                return 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    res = max(res, area)
        
        return res