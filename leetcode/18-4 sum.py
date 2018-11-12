from collections import defaultdict

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = set()

        if sum(nums[0: 4]) > target:
            return []

        for i in range(3, n):
            if sum(nums[i - 3: i + 1]) < target:
                continue

            for j in range(2, i):
                if sum(nums[j - 2: j + 1]) + nums[i] < target:
                    continue
                if sum(nums[0:3]) + nums[i] > target:
                    break

                l, r = 0, j - 1
                while l < r:
                    sum_lr = sum((nums[i], nums[j], nums[l], nums[r]))
                    if sum_lr == target:
                        result.add((nums[l], nums[r], nums[j], nums[i]))
                        l += 1
                        r -= 1
                    elif sum_lr > target:
                        r -= 1
                    else:
                        l += 1

        return list(result)

        
                
s = Solution()

r = s.fourSum([-2, -1, 0, 1, 2, 3, 4], 3)
print(r)

r = s.fourSum([1, 0, -1, 0, -2, 2], 0)
print(r)

                


