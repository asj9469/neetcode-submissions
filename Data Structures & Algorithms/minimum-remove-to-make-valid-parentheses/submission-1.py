class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # any excess (( we have by the end, delete
        # any ) that does not close off a ( - up front, delete

        stack = [] # to store the indices of the ( -> for position tracking
        s = list(s)

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif stack and c == ")":
                stack.pop()
            elif not stack and c == ")":
                s[i] = ""
            elif c.isalpha() and c.islower():
                continue
        
        # whatever gets left in the stack is a leftover (
        # remove ( from the back
        for i, c in enumerate(reversed(s)):
            if not stack:
                break
            else:
                if c == "(":
                    s[len(s)-1-i]=""
                    stack.pop()
        
        return "".join(s)
