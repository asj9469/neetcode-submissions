class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            '2': ["a","b","c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if not digits:
            return []
            
        res = []
        def dfs(string):
            # base case
            if len(string) == len(digits):
                res.append(string)
                return True
            
            # dfs -> iterate through the options
            for option in letter_map[digits[len(string)]]:
                dfs(string + option)
        
        dfs("")
        return res