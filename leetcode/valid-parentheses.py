class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()
        par = {"(": ")", "{": "}", "[":"]"}

        for c in s:
            if c in par:
                stack.append(par[c])

            else:
                if not stack or stack.pop() != str(c):
                    return False

        return not stack