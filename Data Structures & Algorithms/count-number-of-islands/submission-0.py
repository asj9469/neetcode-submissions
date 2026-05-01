from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n, m = len(grid), len(grid[0])
        visited = [[0 for i in range(m)] for j in range(n)]
        print(visited)

        # modify the input to avoid creating a visted set
        count = 0

        # the main function of bfs is to mark the visited ones
        def bfs(i, j):
            q = deque([(i,j)])
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            while q:
                ey, ex = q.popleft()

                for dy, dx in dirs:
                    nx = ex + dx
                    ny = ey + dy

                    # if the new coordinate is within bounds
                    if 0 <= ny < n and 0 <= nx < m:
                        # if the new coordinate isnt visited yet
                        if visited[ny][nx] == 0 and grid[ny][nx] == '1':
                            visited[ny][nx] = 1
                            q.append([ny, nx])

        for i in range(n):
            for j in range(m):
                # if already visited => skip over
                # if not visited & 1, start search
                if visited[i][j] == 0 and grid[i][j] == '1':
                    # if we found an island, update the grid using bfs & increment count
                    visited[i][j] = 1
                    
                    # count the island & mark everything else as visited & move on
                    count += 1
                    print('adding count')
                    bfs(i, j)
        
        return count
