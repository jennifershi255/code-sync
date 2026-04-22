class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        row = len(grid)
        cols = len(grid[0])
        res = 0

        def dfs(r, c):
            if r >= 0 and r < row and c >= 0 and c < cols and grid[r][c] == '1':
                    grid[r][c] = '0'
                    dfs(r + 1, c)
                    dfs(r - 1, c)
                    dfs(r, c + 1)
                    dfs(r, c - 1)
            else:
                return 

        for r in range(row):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r,c)
                    res += 1
        
        return res