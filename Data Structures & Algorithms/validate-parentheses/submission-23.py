class Solution:
    def isValid(self, s: str) -> bool:
        
        closingBrackets = {
            '}' : '{',
            ']' : '[',
            ')' : '(',
        }

        stack = []

        for bracket in s:
            if bracket in closingBrackets:
                if not stack:
                    return False
                else:
                    openingBracket = stack.pop()
                    if closingBrackets[bracket] != openingBracket:
                        return False
            else:
                stack.append(bracket)
                
                
        if stack:
            return False
        else:
            return True