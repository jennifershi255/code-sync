class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        res = 0
        seen_pairs = set()
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            left = i + 1
            right = len(sorted_nums) - 1

            while left <= right:  
                middle = (left + right) // 2
                curr = abs(sorted_nums[i] - sorted_nums[middle])

                if curr == k:
                    pair = (sorted_nums[i], sorted_nums[middle])
                    if pair not in seen_pairs:
                        seen_pairs.add(pair)
                        res += 1
                    break  

                elif curr < k:
                    left = middle + 1
                else:
                    right = middle - 1

        return res