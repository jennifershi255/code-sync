class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        longest = 0
        dups = set()

        for right in range(len(s)):

            while s[right] in dups:
                dups.remove(s[left])
                left += 1
            
            dups.add(s[right])
            length = right - left + 1
            longest = max(longest, length)
        
        return longest