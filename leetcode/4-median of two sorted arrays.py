class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        n = len(nums1)
        m = len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        if not nums1:
            return (nums2[(m - 1) // 2] + nums2[m // 2]) / 2

        max_int = max(nums1[-1], nums2[-1])
        min_int = min(nums1[0], nums2[0])

        l = 0
        h = n * 2
        while l <= h:
            c1 = int((l + h) / 2)
            c2 = m + n - c1

            if c1 == 0:
                l1 = min_int
            else:
                l1 = nums1[(c1 - 1) // 2]

            if c2 == 0:
                l2 = min_int
            else:
                l2 = nums2[(c2 - 1) // 2]

            if c1 == n * 2:
                r1 = max_int
            else:
                r1 = nums1[c1 // 2]
            
            if c2 == m * 2:
                r2 = max_int
            else:
                r2 = nums2[c2 // 2]

            if l1 > r2:
                h = c1 - 1
            elif l2 > r1:
                l = c1 + 1
            else:
                return (max(l1, l2) + min(r1, r2)) / 2
        
        return -1


s = Solution()
# r = s.findMedianSortedArrays([1, 3], [2])
r = s.findMedianSortedArrays([1], [])

print('\r\nMedian of Arrays is: {0}'.format(r))

