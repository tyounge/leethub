class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        global n, m
        n = len(grid)
        m = len(grid[0])
        def dfs(x, y):
            global n, m
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            return 1 + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)
            
        answer = 0
        for i in range(n):
            for j in range(m):
                answer = max(dfs(i,j), answer)
        return answer