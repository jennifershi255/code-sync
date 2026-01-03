class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        res = ""
        min_length = float("inf")

        left = 0
        freqt = defaultdict(int)
        freqs = defaultdict(int)

        for c in t:
            freqt[c] += 1

        def window_valid():
            for c in freqt:
                if freqs[c] < freqt[c]:
                    return False
            return True

        for right in range(len(s)):
            freqs[s[right]] += 1

            while window_valid():
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    res = s[left:right + 1]
                
                freqs[s[left]] -= 1
                left += 1
        
        return res