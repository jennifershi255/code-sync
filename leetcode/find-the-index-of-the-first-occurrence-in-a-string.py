class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        left = 0
        right = len(needle)

        while right <= len(haystack):
            
            if haystack[left:right] == needle:
                return left
            else:
                left += 1
                right += 1
        
        return -1