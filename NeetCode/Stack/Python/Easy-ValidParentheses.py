class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {'}':'{', ']':'[', ')':'('}

        for i in s:
            if i == '{' or i == '[' or i == '(':
                stack.append(i)
            else:
                if len(stack) > 0 and stack[-1] == openToClose[i]:
                    stack.pop()
                    continue
                
                return False
            
        return False if stack else True