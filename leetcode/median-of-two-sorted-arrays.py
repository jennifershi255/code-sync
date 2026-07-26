class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        l1 = [ ... maxLeft1 | minRight1 ...]
        l2 = [ ... maxLeft2 | minRight2 ...]

        """

        # set nums1 to be the shorter one
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)

        # if odd length, extra value goes on left partition
        half = (m+n+1) // 2

        lo, hi = 0, m

        while lo <= hi:
            p1 = (lo + hi) // 2 
            p2 = half - p1

            maxLeft1 = float('-inf') if p1 == 0 else nums1[p1-1]
            minRight1 = float('inf') if p1 == m else nums1[p1]
            maxLeft2 = float('-inf') if p2 == 0 else nums2[p2-1]
            minRight2 = float('inf') if p2 == n else nums2[p2]

            if (maxLeft1 <= minRight2 and maxLeft2 <= minRight1): #valid
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                else:
                    return max(maxLeft1, maxLeft2)
            if maxLeft1 > minRight2: # left partition too far left, move right (smaller)
                hi = p1 - 1
            elif maxLeft2 > minRight1: # right1 partition too far right, make it bigger
                lo = p1 + 1