from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 
        row , col = len(grid) , len(grid[0])
        visited = set()
        island = 0

        def bfs(r , c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            
            while q :
                r , c = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    rows , cols = r + dr , c + dc
                    if (rows in range(len(grid))and cols in range(len(grid[0]))and grid[rows][cols]=='1' and (rows , cols) not in visited):
                        q.append((rows,cols))
                        visited.add((rows,cols))


        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i , j) not in visited:
                    bfs(i,j)
                    island +=1
        return island        