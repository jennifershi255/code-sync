class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()
        par = {"(": ")", "{": "}", "[":"]"}

        if len(s) % 2 != 0:
            return False

        for c in s:
            
            if c in par:
                stack.append(par[c])
                continue

            if stack:
                popped = stack.pop()
                
                if (popped != str(c)):
                    return False
            elif c not in par:
                return False
        
        if not stack:
            return True
        else:
            return False