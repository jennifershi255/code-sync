class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = ""
        isNeg = 1
        i = 0

        if len(s) == 0:
            return 0

        while i < len(s) and (s[i] == " " or s[i] == "-" or s[i] == "+"):
            if s[i] == " ":
                i += 1
                continue
            if s[i] == "-":
                isNeg *= -1
                i += 1
                break
            elif s[i] == "+":
                i += 1
                break

        while i < len(s) and s[i].isdigit():
            while s[i] == 0:
                i += 1
                continue
            
            res += s[i]
            i += 1

        if res:
            res = int(res) * isNeg
            
            if res <= (-2)**31:
                return (-2)**31
            elif res >= (2**31 - 1):
                return (2**31 - 1)
            else:
                return res
        else:
            return 0