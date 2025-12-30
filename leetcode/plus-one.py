class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = int("".join(str(i) for i in digits))
        num += 1
        res = list(map(int, str(num)))
        return res