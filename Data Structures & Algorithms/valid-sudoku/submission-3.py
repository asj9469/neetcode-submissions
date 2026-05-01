class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # case 1
        # 1. check if the given 3x3 grid is valid

        def isValidSmallGrid(sg):
            # small grid will be 3x3
            # early return if we see a duplicate
            seen = set() # won't affect space complexity bc at most 9

            for i in range(3):
                for j in range(3):
                    if sg[i][j] in seen and sg[i][j] != ".":
                        return False
                    # print(seen)
                    seen.add(sg[i][j])
            return True

        def isValidRowCol(ls):
            seen = set()
            for i in ls:
                if i in seen:
                    return False
                if i != "." and 9 >= int(i) <= 0: # out of range
                    return False
                if i != ".":
                    seen.add(i)
            return True
        # check each column -> only have to check when i = 0
        # check each row
        # -> can be combined & result in O(n) = O(9) = O(1)
        for i in range(9):
            if not isValidRowCol(board[i]):
                print('failed at row')
                return False
            
            # recycle this i to act like a j
            col = [board[x][i] for x in range(9)]
            if not isValidRowCol(col):
                print('failed at col')
                return False

        # first go through all the 3x3 small grids
        for i in range(0,9,3):
            for j in range(0,9,3):
                sg = [board[x][j:j+3] for x in range(i, i+3)]
                if not isValidSmallGrid(sg):
                    print('failed at small grid')
                    return False
            
        return True
