class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = sorted(nums)
        n = len(l)
        combinations = []

        for i in (range(2, n)):
            if l[i] < 0:
                continue

            if sum(l[i - 2: i + 1]) < 0:
                continue

            break
        else:
            return combinations

        ti = l[i - 2] - 1
        for i in range(i - 2, n):
            if l[i] = ti:
                continue

            tj = l[i + 1] - 1
            for j in range(i + 1, n):
                if l[j] == tj:
                    continue

                tk = l[j + 1] - 1
                for k in range(j + 1, n):
                    if l[k] == tk:
                        continue
                    
                    combinations.append((l[i], l[j], [k]))

                tj = l[j]
            ti = l[i]

        return combinations
            


            

