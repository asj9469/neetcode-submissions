class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # at each cell, we need to do a DFS
        # keep track of which index of word we're searching for

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        # i, j => positioning on board
        # k => index on word

        # objective: see if board[i][j] == word[k]
        def explore(i, j, k):
            # base cases
            if k == len(word):
                # we already reached the end of the word, mission complete
                return True
            # bound check
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            # if letter is not a match
            if board[i][j] != word[k]:
                return False
            
            # need to check if visited
            if (i,j) in visited:
                return False

            # before visiting, we mark current one as visited
            visited.add((i,j))
            for dy, dx in dirs:
                if explore(i + dy, j + dx, k + 1):
                    return True

            # all children failed
            visited.remove((i,j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if explore(i,j,0):
                    return True
            
        return False