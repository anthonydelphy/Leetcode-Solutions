class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # While the stack contains items less the current date,
            # Pop from stack until a higher temp date is found or until
            # the stack is empty.
            while stack and t > temperatures[stack[-1]]:
                val = stack.pop()
                result[val] = i - val
    
            stack.append(i)

        return result