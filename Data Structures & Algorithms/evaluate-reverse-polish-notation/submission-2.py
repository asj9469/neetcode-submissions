class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use stack

        operators = set(['+', '-', '*', '/'])
        stack = []

        for t in tokens:
            print("current stack", stack)
            if t in operators:
                if stack:
                    # need to pop out the two, and append back the results
                    num1, num2 = stack.pop(), stack.pop()
                    if t == "+":
                        stack.append(num2+num1)
                    elif t == "-":
                        stack.append(num2-num1)
                    elif t == "*":
                        stack.append(num2*num1)
                    elif t == "/":
                        stack.append(int(num2 / num1))
            else:
                stack.append(int(t))
        return stack.pop()