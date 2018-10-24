import numpy as np

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # r_border is the right border that have been explored
        r_border = 0
        # pivot is the center of palindromic substring defined by r_border
        pivot = 0

        dp = np.ones(2 * n + 1, dtype=np.int)

        # Change string to form [# a # b # a #], and we do not need to check # at head or tail
        for p in range(1, n * 2):
            if p < r_border:
                i = 2 * pivot - p
                dp[p] = min(dp[i], r_border - p + 1)
            else:
                dp[p] = 1 - p % 2
            
            for k in range(0, min(p, 2 * n - p, 2)):
                if s[(p - 2 * k - 1) // 2] != s[(p + 2 * k) // 2]:
                    break
                dp[p] += 2

            r_explored = (p + dp[p] - 1)
            if r_border < r_explored:
                r_border = r_explored
                pivot = p

        return dp[p]

            
s = Solution()

r1 = s.longestPalindrome("aa")
print(r1)

r2 = s.longestPalindrome("aba")
print(r2)

pass

