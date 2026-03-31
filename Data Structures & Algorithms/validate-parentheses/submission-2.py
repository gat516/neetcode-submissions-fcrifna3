class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { ")" : "(", "]" : "[", "}": "{"} 

        #stack is last in first out.
        # ( {  [  ]  } )
        # (, ( {, ( { [, ( { [,

        for c in s: 
            stack
            if c in pairs: #if its a closing bracket, pop
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        else:
            return True


