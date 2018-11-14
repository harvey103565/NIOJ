class Solution:

    def __init__(self):
        self.dp = dict(zip((0, 1), ([''], ['()'])))

    def generateParenthesis_optimum(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def parenthese(n):
            if n not in self.dp:
                self.dp[n] = ['(' + sl + ')' + sr for m in range(n) for sl in parenthese(m) for sr in parenthese((n - 1) - m)]
            
            return self.dp[n]

        return parenthese(n)

    def generateParenthesis_opt(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [None] * (n + 1)
        dp[0] = ['']
        for i in range(1, n + 1):                   # length
            dp[i] = []
            for j in range(1, i + 1):               # division
                for sl in dp[j - 1]:                    # left part of string
                    for sr in dp[i - j]:        # right part of string
                        dp[i].append('(' + sl + ')' + sr)
        
        return dp[n]


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def parenthese(n):
            if n == 0:
                yield ''
                return

            if n == 1:
                yield '()'
                return

            for m in range(n):
                yield from ('({0}){1}'.format(sl, sr) for sl in parenthese(m) for sr in parenthese(n - m - 1))

        return [s for s in parenthese(n)]


s = Solution()

r = s.generateParenthesis_optimum(1)
print(r)
                
r = s.generateParenthesis_optimum(2)
print(r)
                
r = s.generateParenthesis_optimum(3)
print(r)
                
