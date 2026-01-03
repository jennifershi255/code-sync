class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        left = 0
        right = len(s1) - 1

        freqs1 = defaultdict(int)
        freqs2 = defaultdict(int)

        for i in range(len(s1)):
            freqs1[s1[i]] += 1

        for i in range(len(s1)):
            freqs2[s2[i]] += 1

        while right < len(s2):
            if freqs1 == freqs2:
                return True 
            
            freqs2[s2[left]] -= 1
            if freqs2[s2[left]] == 0:
                del freqs2[s2[left]]
            left += 1
            right += 1
            if right < len(s2):
                freqs2[s2[right]] += 1
    
        return False