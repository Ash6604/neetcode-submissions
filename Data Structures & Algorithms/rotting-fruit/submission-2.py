from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0
        row , col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while q and fresh > 0 :
            for i in range(len(q)):
                r,c = q.popleft()

                for dr ,dc in directions :
                    rows = r + dr
                    cols = c + dc

                    if (rows in range(len(grid)) and cols in range(len(grid[0])) and grid[rows][cols]==1):
                        grid[rows][cols] = 2
                        q.append((rows,cols))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

        