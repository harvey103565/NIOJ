import numpy as np


class Knapsack:
    def __init__(self, volume: int):
        self._volume = volume

    def wrap(self, value: list, cost: list) -> list:
        """
            : Most ordinary way to solve this problem. There is a sack with volumn of v and some i items. Choose
            the larger one between dp[i - 1][v - cost[i]] + value[i] and dp[i - 1][v]. The former one means that
            we put i-th item into the sack then we got a (new) sack with the volumn of v - cost[i] and the problem
            is turned into i - 1 scale sub-problem, which we have sovled in formmer loop. The later one means that
            the i-th item is ignore, we also check the result of i - 1 sub-problem, but with the volumn of sack of v.
        """
        n = len(value)

        dp = np.zeros((n, self._volume + 1), dtype=np.int)
        for i in range(n):
            for j in range(self._volume + 1):
                if j >= cost[i]:
                    dp[i][j] = max((dp[i - 1][j - cost[i]] + value[i]), dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp

    def wrap_opt(self, value: list, cost: list) -> list:
        """
            : An optimized way. Since each time we just need to check dp[i - 1] which is i - 1 scale sub-problem. 
            So it is not neccessary to save result of sub-problem earlier than i - 1. In order to save memory,
            we use one demension array here. HOWEVER: we must write from the END OF ARRAY to avoid overwriting to the 
            result of former sub-problem.
        """
        n = len(value)

        dp = np.zeros(self._volume + 1, dtype=np.int)

        for i in range(n):
            for j in range(self._volume, cost[i] - 1, -1):
                if j >= cost[i]:
                    dp[j] = max(dp[j - cost[i]] + value[i], dp[j])

        return dp
    

knapsack = Knapsack(15)

r1 = knapsack.wrap((12, 3, 10, 3, 6), (5, 4, 7, 2, 6))
print(r1)

r2 = knapsack.wrap_opt((12, 3, 10, 3, 6), (5, 4, 7, 2, 6))
print(r2)

pass
