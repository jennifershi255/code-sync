class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        for f in freq:
            if freq[f] == 1:
                return f