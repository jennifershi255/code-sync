class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        length = len(s) - 1

        while (s[length] == " "):
            length -= 1

        while (s[length] != " " and length >= 0):
            count += 1
            length -= 1

        return count