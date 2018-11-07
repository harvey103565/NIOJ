import numpy as np


class Knapsack:
    def __init__(self, volume: int):
        self._volume = volume

    def wrap(self, v: tuple, w: tuple) -> np.ndarray:
        """
            : Most ordinary way to solve this problem. There is a sack with volumn of v and some i items. Choose
            the larger one between dp[i - 1][v - size[i]] + value[i] and dp[i - 1][v]. The former one means that
            we put i-th item into the sack then we got a (new) sack with the volumn of v - size[i] and the problem
            is turned into i - 1 scale sub-problem, which we have sovled in formmer loop. The later one means that
            the i-th item is ignore, we also check the result of i - 1 sub-problem, but with the volumn of sack of v.
        """
        n = len(v)
        # TODO: Argument checking
        dp = np.zeros((n, self._volume + 1), dtype=np.int)

        for i in range(n):
            for W in range(self._volume + 1):
                if W >= w[i]:
                    dp[i][W] = max((dp[i - 1][W - w[i]] + v[i]), dp[i - 1][W])
                else:
                    dp[i][W] = dp[i - 1][W]

        return dp

    def wrap_opt(self, v: tuple, w: tuple) -> np.ndarray:
        """
            : An optimized way. Since each time we just need to check dp[i - 1] which is i - 1 scale sub-problem. 
            So it is not neccessary to save result of sub-problem earlier than i - 1. In order to save memory,
            we use one demension array here. HOWEVER: we must write from the END OF ARRAY to avoid overwriting to the 
            result of former sub-problem.
        """
        n = len(v)
        # TODO: Argument checking
        dp = np.zeros(self._volume + 1, dtype=np.int)

        for i in range(n):
            for W in range(self._volume, w[i] - 1, -1):
                dp[W] = max(dp[W - w[i]] + v[i], dp[W])

        return dp
    
    def warp_opt_exact_match(self, v: tuple, size: tuple) -> np.ndarray:
        """
        """
        n = len(v)
        # TODO: Argument checking
        dp = np.array([-1] * (self._volume + 1), dtype=np.int)

        for i in range(n):
            for W in range(self._volume, size[i] - 1, -1):
                if W == size[i]:
                    dp[W] = max(dp[W], v[i])
                elif dp[W - size[i]] != -1:
                    dp[W] = max(dp[W - size[i]] + v[i], dp[W])
        
        return dp


knapsack = Knapsack(15)

r1 = knapsack.wrap((12, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r1)

r2 = knapsack.wrap_opt((12, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r2)

r3 = knapsack.warp_opt_exact_match((12, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r3)

pass
