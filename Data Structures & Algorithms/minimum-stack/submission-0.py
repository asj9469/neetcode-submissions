class MinStack:

    def __init__(self):
        self.stack = [] # [ (-2, -2), (0, -2), (-3, -3) ]

    def push(self, val: int) -> None:
        min_so_far = self.stack[-1][1] if self.stack else val
        self.stack.append((val, min(val, min_so_far)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
