# The idea behind this is to have two stacks.
# One is the primary stack with standard stack method. 
# There is an auxillary stack utilized to capture the Min at 
# each level of the stack. If we pop from the main stack,
# we also must pop from the auxillary minStack.
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
