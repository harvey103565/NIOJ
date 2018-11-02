class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_size = 0
        while j > i:
            if height[i] > height[j]:
                max_size = max(max_size, height[j] * (j - i))
                j -= 1
            else:
                max_size = max(max_size, height[i] * (j - i))
                i += 1
            
        return max_size


s = Solution()

r = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(r)

r = s.maxArea([5, 9, 4, 2, 7, 4, 8])
print(r)

r = s.maxArea([5, 3, 6, 9, 4, 2, 1, 7, 6, 8])
print(r)
