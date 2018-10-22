import numpy as np

class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        n = len(name)
        m = len(typed)

        dp = np.zeros((n + 1, m + 1), dtype=np.bool)
        dp[0][0] = True

        for i in range(n):
            for j in range(m):
                dp[i + 1][j + 1] = (typed[j] == name[i] and (dp[i][j] or dp[i + 1][j]))
        
        return dp[n][m]


s = Solution()

r1 =  s.isLongPressedName("alex", "aaleex")
print(r1)

r2 =  s.isLongPressedName("saeed", "ssaaedd")
print(r2)

r3 =  s.isLongPressedName("leelee", "lleeelee")
print(r3)

r4 =  s.isLongPressedName("laiden", "laiden")
print(r4)

r5 =  s.isLongPressedName("vtkgn", "vttkgnn")
print(r5)

pass        