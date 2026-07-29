class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            ')' :'(',
            "}" : '{',
            ']' : '['
        }
        

        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if top != brackets[char]:
                    return False
        return len(stack) == 0            

