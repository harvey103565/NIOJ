import numpy as np


class Knapsack:
    def __init__(self, volume: int):
        self._volume = volume

    def ZeroOneSack(self, v: iter, c: iter) -> list:
        n = len(v)

        dp = np.zeros((n, self._volume + 1), dtype=np.int)
        for j in range(self._volume + 1):
            if j >= c[0]:
                dp[0][j] = v[0]
        
        for i in range(1, n):
            for j in range(self._volume + 1):
                if j + 1 > c[i]:
                    dp[i][j] = max((dp[i - 1][j - c[i]] + v[i]), dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp

    def ZeroOneSack_Opt(self, v: list, c: list) -> list:
        n = len(v)

        dp = np.zeros(self._volume + 1, dtype=np.int)

        for i in range(n):
            for j in range(self._volume, 0, -1):
                if j > c[i]:
                    dp[j] = max(dp[j - c[i]] + v[i], dp[j])

        return dp
    

knapsack = Knapsack(15)

r1 = knapsack.ZeroOneSack((12, 3, 10, 3, 6), (5, 4, 7, 2, 6))
r2 = knapsack.ZeroOneSack_Opt((12, 3, 10, 3, 6), (5, 4, 7, 2, 6))
print(r1)
print(r2)

pass
