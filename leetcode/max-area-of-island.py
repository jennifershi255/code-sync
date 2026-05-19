class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        
        def dfs(r,c,total):

            if r >= 0 and r < ROWS and c >= 0 and c < COLS and grid[r][c] == 1:
                grid[r][c] = 0
                return 1 + dfs(r-1,c,total) + dfs(r+1,c,total) + dfs(r,c-1,total) + dfs(r,c+1,total) 
            
            else:
                return 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r,c,0)
                    res = max(area,res)
        
        return res