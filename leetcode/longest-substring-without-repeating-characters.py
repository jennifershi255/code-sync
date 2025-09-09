class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remember for DYNAMIC SLIDING WINDOW problems to set right pointer to increment in the for loop
        
        dups = set()
        left = 0
        longest = 0
        
        for right in range(len(s)):

            while s[right] in dups:
                dups.remove(s[left])
                left += 1

            dups.add(s[right])
            longest = max(longest, right - left + 1)
            right += 1

        return longest
