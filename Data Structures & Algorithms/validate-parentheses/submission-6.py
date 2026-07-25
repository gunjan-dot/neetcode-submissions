class Solution:
    def isValid(self, s: str) -> bool:
        braces = {')':'(', ']':'[', '}':'{'}
        stack = []

        for i in s:
            if i in braces.values():
                stack.append(i)
            elif i in braces:
                if not stack or stack[-1] != braces[i]:
                    return False 
                stack.pop()      
            else:
                return False 
        return len(stack) == 0

        