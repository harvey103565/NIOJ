import numpy as np


class Knapsack:
    def __init__(self, volume: int):
        self._volume = volume

    def ZeroOneSack(self, v: iter, c: iter) -> list:
        cnt = len(v)

        dp = np.zeros((cnt, self._volume + 1), dtype=np.int)
        # dp = [[0] * self._volume] * cnt
        for j in range(self._volume + 1):
            if j >= c[0]:
                dp[0][j] = v[0]
        
        for i in range(1, cnt):
            for j in range(self._volume + 1):
                if j + 1 > c[i]:
                    dp[i][j] = max((dp[i - 1][j - c[i]] + v[i]), dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp

    def ZeroOneSack_Opt(self, v: list, c: list) -> list:
        return None
    

knapsack = Knapsack(15)

r = knapsack.ZeroOneSack((12, 3, 10, 3, 6), (5, 4, 7, 2, 6))
print(r)

