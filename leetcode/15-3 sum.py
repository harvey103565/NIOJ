class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        result = []

        def binary_seek(a: list, k: int, l: int, r: int):
            p = (l + r) // 2
            while(l < r):
                if a[p] > k:
                    r = p
                elif a[p] < k:
                    l = p + 1
                else:
                    break
                p = (l + r) // 2
            return p

        def move_next(a: list, s: int, e: int, d: int) -> int:
            v = a[s]
            while a[s] == v and s != e:
                s = s + d
            return s

        l, r = 0, n - 1
        while l < r - 1:
            i, k = l, r
            while i < k - 1:
                target_sum = -(sorted_nums[i] + sorted_nums[r])

                if sorted_nums[i] <= target_sum <= sorted_nums[r]:
                    k = binary_seek(sorted_nums, target_sum, i + 1, k - 1)
                    if sorted_nums[k] > target_sum:
                        r = move_next(sorted_nums, r, l + 1, -1)
                        break
                    else:
                        if sorted_nums[k] == target_sum:
                            result.append((sorted_nums[i], sorted_nums[k], sorted_nums[r]))
                        else:
                            k += 1
                        i = move_next(sorted_nums, i, k, 1)
                else:
                    if target_sum > sorted_nums[r]:
                        l = move_next(sorted_nums, l, k, 1)
                    else:
                        r = move_next(sorted_nums, r, l + 1, -1)
                    break
            else:
                r = move_next(sorted_nums, r, l + 1, -1)

        return result



s = Solution()

r = s.threeSum([-1, 0, 1, 2, -1, -4])
print(r)

r = s.threeSum([0, 0, 0, 0, 0, 0])
print(r)

r = s.threeSum([3,0,-2,-1,1,2])
print(r)

r = s.threeSum([-4,-1,-4,0,2,-2,-4,-3,2,-3,2,3,3,-4])
print(r)

pass
