class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i, n = 0, len(nums)
        result = sum(nums[:3])
        delta = abs(target - result)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                t_min = nums[i] + nums[l] + nums[l + 1]
                t_max = nums[i] + nums[r] + nums[r - 1]
                t = nums[i] + nums[l] + nums[r]

                if t_max < target:
                    d = abs(t_max - target)
                    if d < delta:
                        result = t_max
                        delta = d
                    break

                if t_min > target:
                    d = abs(t_min - target)
                    if d < delta:
                        result = t_min
                        delta = d
                    break

                d = abs(t - target)
                if d < delta:
                    result = t
                    delta = d

                if t > target:
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif t < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    return t

        return result


s = Solution()

r = s.threeSumClosest([0, 2, 1, -3], 1)
print(r)

r = s.threeSumClosest([-1, 2, 1, -4], -2)
print(r)

r = s.threeSumClosest([-1, 0, 1, 2, -1, -4], -2)
print(r)

r = s.threeSumClosest([-1, 0, 1, 2, -1, -4], -3)
print(r)

r = s.threeSumClosest([0, 0, 0, 0, 0, 0], 0)
print(r)

r = s.threeSumClosest([3, 0, -2, -1, 1, 2], 1)
print(r)

r = s.threeSumClosest([-4, -1, -4, 0, 2, -2, -4, -3, 2, -3, 2, 3, 3, -4], -5)
print(r)

