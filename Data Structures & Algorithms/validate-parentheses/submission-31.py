class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        #stack = [ (   
        #stack = [ ([
        #stack = [ ([{
        #when we see a closing bracket, pop.
        #we've taken in }, so pop

        closeToOpen = { 
            '}' : '{' , 
            ')' : '(', 
            ']' : '['
        }

        for c in s:
            #if c is not a closing bracket
            
            if c not in closeToOpen:
                stack.append(c)
            elif c in closeToOpen and stack:
                openingBracket = stack.pop()
                if openingBracket != closeToOpen[c]:
                    return False
            elif c in closeToOpen:
                return False


        return not stack


