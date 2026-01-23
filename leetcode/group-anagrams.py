class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        res = []

        for i in range(len(strs)):
            word = strs[i]
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            
            if not tuple(count) in anagrams:
                anagrams[tuple(count)] = [word]
            else:
                anagrams[tuple(count)].append(word)
        
        for k,v in anagrams.items():
            res.append(v)
        
        return res