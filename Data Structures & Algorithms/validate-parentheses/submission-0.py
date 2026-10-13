class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')':'(', ']':'[', '}':'{'}
        paren = '({['
        stack = []

        for char in s:
            if char in paren:
                stack.append(char)
            else:
                if not stack:
                    return False
                
                if stack.pop() != valid[char]:
                    return False
                
        return not stack