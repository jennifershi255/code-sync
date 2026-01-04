class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        left = 0
        window = deque()

        for right in range(len(nums)):
            while window and nums[window[-1]] < nums[right]:
                window.pop()

            window.append(right)

            if window[0] < left:
                window.popleft()
            
            if right - left + 1 == k:
                res.append(nums[window[0]])
                left += 1
        
        return res