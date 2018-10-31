from sys import maxsize

min_int = -maxsize - 1
max_int = maxsize

class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        sum_array = cur_max = cur_min = 0
        max_sum = min_int
        min_sum = max_int

        for n in A:
            cur_max = n + max(cur_max, 0)
            max_sum = max(max_sum, cur_max)
            
            cur_min = n + min(cur_min, 0)
            min_sum = min(min_sum, cur_min)
            
            sum_array += n

        if sum_array > min_sum:
            return max(max_sum, sum_array - min_sum)
        else:
            return max_sum


s = Solution()

r = s.maxSubarraySumCircular([1])
print(r)

r = s.maxSubarraySumCircular([1, 2, -1])
print(r)

r = s.maxSubarraySumCircular([1, -2, 3, -2])
print(r)

r = s.maxSubarraySumCircular([5, -3, 5])
print(r)

r = s.maxSubarraySumCircular([3, -1, 2, -1])
print(r)

r = s.maxSubarraySumCircular([3, -2, 2, -3])
print(r)

r = s.maxSubarraySumCircular([-2, -3, -1])
print(r)


