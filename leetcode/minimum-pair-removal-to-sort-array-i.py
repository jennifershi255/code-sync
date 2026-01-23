class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        ops = 0

        def is_sorted(arr):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    return False
            
            return True

        while not is_sorted(nums):
            lowest = float("inf")
            lowestI = 0
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]

                if s < lowest:
                    lowest = s
                    lowestI = i
            
            nums[lowestI:lowestI+2] = [lowest]
            ops += 1
            
        return ops