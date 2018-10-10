


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        dp = [[False if i or j else True for i in range(n + 1)] for j in range(m + 1)]

        for i in range(m):
            dp[i + 1][0] = dp[i -1][0] and p[i] == '*'
            for j in range(n):
                if p[i] == '*':
                    dp[i + 1][j + 1] = (dp[i - 1][j + 1] or dp[i][j + 1] or ((p[i - 1] == s[j] or p[i - 1] == '.') and dp[i + 1][j]))
                else:
                    dp[i + 1][j + 1] = ((p[i] == s[j] or p[i] == '.') and dp[i][j])
        return dp[m][n]



s = Solution()

r = s.isMatch("aa", "aaa")
r = s.isMatch("aaa", "aa")
r = s.isMatch("aa", "a*a")
r = s.isMatch("aaa", "a*aaa")
r = s.isMatch("ac", ".*")
r = s.isMatch("ac", "ab")
r = s.isMatch("abc", "abc")
r = s.isMatch("bc", "a*bc")
r = s.isMatch("aabc", "a*bc")
r = s.isMatch("aabc", "a*abc")
r = s.isMatch("aabc", "a*aabc")
r = s.isMatch("abc", "a*b*c*")
r = s.isMatch("abc", "a*b*c*c")
r = s.isMatch("abc", "a*b*c*bc")
r = s.isMatch("abc", "a*b*c*.")

pass