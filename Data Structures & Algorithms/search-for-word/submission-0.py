class Solution:
    def exist(self, board: List[List[str]], word: str):
        
        # options are the 4 directions

        visited = set() # tracking visited cells
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def explore(i, j, k):
            if k == len(word): # length is satisfied
                return True

            # did we already visit?
            if (i, j) in visited:
                return False

            # check boundaries
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return False

            # the board position is not matching the current index character
            if word[k] != board[i][j]:
                return False

            # mark as visited
            visited.add((i,j))

            # now we explore all 4 directions
            for di, dj in dirs:
                ei, ej = i + di, j + dj
                if explore(ei, ej, k+1): # 여기서 계속 뻉뻉이 돌다가 밑으로
                    # don't understand this part
                    # visited.remove((i,j))
                    return True

            # backtracking => removing it from visited (can explore again)
            visited.remove((i,j))
            return False
    
        for i in range(len(board)):
            for j in range(len(board[i])):
                if explore(i, j, 0):
                    return True
        return False