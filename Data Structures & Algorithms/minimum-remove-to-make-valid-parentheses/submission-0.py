class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = [] # running stack of the parentheses

        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''

        # by this point, we will have a stack of parentheses & string with no extra )
        # case 1: stack is actually empty -> we're good
        # case 2: stack is not empty = not enough closing parentheses [(, (]
        #   extra parentheses towards the end

        if not stack:
            return ''.join(s)

        if stack:
            for i, c in enumerate(reversed(s)):
                if c == '(' and stack:
                    print(c)
                    stack.pop()
                    s[len(s)-1-i] = ''
        
        return ''.join(s)