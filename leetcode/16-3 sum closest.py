class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        result = sum(nums[:3])

        for i in range(n):
            k = target - nums[i]

            l, r = i + 1, n - 1
            while l < r:
                t = nums[i] + nums[l] + nums[r]

                if abs(t - target) < abs(result - target):
                    result = t

                if t > target:
                    r -= 1
                elif t < target:
                    l += 1
                else:
                    break
        
        return result


s = Solution()

r = s.threeSumClosest([-1, 0, 1, 2, -1, -4], -2)
print(r)

r = s.threeSumClosest([-1, 0, 1, 2, -1, -4], -3)
print(r)

r = s.threeSumClosest([0, 0, 0, 0, 0, 0], 0)
print(r)

r = s.threeSumClosest([3, 0, -2, -1, 1, 2], 1)
print(r)

r = s.threeSumClosest([-4, -1, -4, 0, 2, -2, -4, -3, 2, -3, 2, 3, 3, -4], -1)
print(r)

