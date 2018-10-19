import numpy as np


class Knapsack:
    def __init__(self, volume: int):
        self._volume = volume

    def wrap(self, value: list, size: list) -> list:
        """
            : Most ordinary way to solve this problem. There is a sack with volumn of v and some i items. Choose
            the larger one between dp[i - 1][v - size[i]] + value[i] and dp[i - 1][v]. The former one means that
            we put i-th item into the sack then we got a (new) sack with the volumn of v - size[i] and the problem
            is turned into i - 1 scale sub-problem, which we have sovled in formmer loop. The later one means that
            the i-th item is ignore, we also check the result of i - 1 sub-problem, but with the volumn of sack of v.
        """
        n = len(value)
        # TODO: Argument checking
        dp = np.zeros((n, self._volume + 1), dtype=np.int)

        for i in range(n):
            for v in range(self._volume + 1):
                if v >= size[i]:
                    dp[i][v] = max((dp[i - 1][v - size[i]] + value[i]), dp[i - 1][v])
                else:
                    dp[i][v] = dp[i - 1][v]

        return dp

    def wrap_opt(self, value: list, size: list) -> list:
        """
            : An optimized way. Since each time we just need to check dp[i - 1] which is i - 1 scale sub-problem. 
            So it is not neccessary to save result of sub-problem earlier than i - 1. In order to save memory,
            we use one demension array here. HOWEVER: we must write from the END OF ARRAY to avoid overwriting to the 
            result of former sub-problem.
        """
        n = len(value)
        # TODO: Argument checking
        dp = np.zeros(self._volume + 1, dtype=np.int)

        for i in range(n):
            for v in range(self._volume, size[i] - 1, -1):
                dp[v] = max(dp[v - size[i]] + value[i], dp[v])

        return dp
    
    def warp_opt_exact_match(self, value: list, size: list) -> list:
        """
        """
        n = len(value)
        # TODO: Argument checking
        dp = np.array([-1] * (self._volume + 1), dtype=np.int)

        for i in range(n):
            for v in range(self._volume, size[i] - 1, -1):
                if v == size[i]:
                    dp[v] = max(dp[v], value[i])
                elif dp[v - size[i]] != -1:
                    dp[v] = max(dp[v - size[i]] + value[i], dp[v])
        
        return dp

knapsack = Knapsack(15)

r1 = knapsack.wrap((12, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r1)

r2 = knapsack.wrap_opt((12, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r2)

r3 = knapsack.warp_opt_exact_match((12, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r3)

pass
