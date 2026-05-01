class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # horizontally or vertically -> up, down, left, right
        max_area = 0

        def getArea(i, j):
            # down, right, up, left
            dirs = [(1,0), (0,1), (-1,0), (0,-1)]
            q = deque()

            ##### THESE TWO SHOULD BE A PAIR ####
            q.append((i,j))
            grid[i][j] = -1 
            # ALWAYS MARK THE CELL VISITED AS SOON AS WE APPEND TO QUEUE
            # this is a RULE OF THUMB to make sure we aren't adding redundant cells to queue

            area = 0

            while q:
                area += 1
                ei, ej = q.popleft()
                
                for di, dj in dirs: # iterating through the direction arr
                    ni, nj = ei + di, ej + dj
                    
                    # if the new coordiantes are valid and not visited
                    if 0 <= ni <= len(grid)-1 and 0 <= nj <= len(grid[0])-1:
                        if grid[ni][nj] == 1:
                            grid[ni][nj] = -1
                            q.append((ni, nj))

            return area

        # mark as visited = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = grid[i][j]
                if curr == 1: # not visited & island
                    # then explore the current island
                    # and get the area of the island
                    max_area = max(max_area, getArea(i,j))
            
        return max_area