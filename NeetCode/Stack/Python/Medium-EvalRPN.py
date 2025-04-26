class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                res = int(stack.pop()) + int(stack.pop())
                stack.append(res)
            elif i == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                res = int(b - a)
                stack.append(res)
            elif i == '*':
                res = int(stack.pop()) * int(stack.pop())
                stack.append(res)
            elif i == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                res = int(b / a)
                stack.append(res)
            else:
                stack.append(i)
        return int(stack.pop())
