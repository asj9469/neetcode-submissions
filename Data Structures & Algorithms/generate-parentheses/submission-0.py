class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def is_valid(string):
            # count the closing brackets
            # ())
            open_cnt, close_cnt = 0, 0

            for c in string:
                if c == "(":
                    open_cnt += 1
                else:
                    close_cnt += 1
            
            if open_cnt < close_cnt or open_cnt > n or close_cnt > n:
                return False

            return True

        res = []
        def dfs(string):
            # base case -> return when the string is complete
            if len(string) == n * 2 and is_valid(string):
                res.append(string) # completed one path, log it
                return True

            # base case #2 -> if invalid
            if not is_valid(string):
                return False

            # make a choice
            options = ['(', ')']
            for option in options:
                dfs(string + option)

        dfs('(')
        return res