class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        arr = []
        for c in s:
            if c != "-":
                if c >= 'a' and c <= 'z':
                    arr.append(str.upper(c))
                else:
                    arr.append(c)
        
        res = ""
        count = 0

        for i in range(len(arr) - 1, -1, -1):
            res += arr[i]
            count += 1
            if count == k:
                res += "-"
                count = 0

        if res and res[-1] == "-":
            res = res[:-1]

        return res[::-1]