import numpy as np

class Knapsack:
    def __init__(self, weight: int):
        self._weight = weight

    def wrap(self, v: tuple, w: tuple) -> np.ndarray:
        """
        Wrap all item into knapsack
            : For complete knapsack problem, every item could be taken as many times as it could be. It's ordinary 
            way to treat such item as a set of sigal ones. Then add them into sack one by one. This turns complete 
            knapsack problem into zero one subtype. Since quantity of each items is actually infinite, so we must use 
            volume / size to determine how many times it could be add. 
            Be noticed that, the dp matrix is extended as items are splitted. However, if we use optimzed method in
            zero one problem, any one demension matrix with the size of v is required. Thus, this is the way.

        """
        n = len(v)
        dp = np.zeros(self._weight + 1, dtype=np.int)
        
        for i in range(n):
            k = self._weight // w[i]
            for l in range(k):
                l = l   # eliminate warning
                for W in range(self._weight, w[i] - 1, -1):
                    dp[W] = max(dp[W - w[i]] + v[i], dp[W])

        return dp

    def wrap_opt(self, v: tuple, w: tuple) -> np.ndarray:
        """
        Wrap all item into knapsack
            : A small optimization. Items are divided following the rule: [1/2, 1/4, 1/8, ... ] rather than [1, 1, 1]
            So the middle loop(the k-loop) run log(n) times instead of n time.

        """
        n = len(v)
        dp = np.zeros(self._weight + 1, dtype=np.int)
        
        for i in range(n):
            k = 1
            l = self._weight // w[i]
            while k <= l:
                for W in range(self._weight, w[i] * k - 1, -1):
                    dp[W] = max(dp[W - w[i] * k] + v[i] * k, dp[W])
                k *= 2

        return dp

    def warp_opt_exact_match(self, v: tuple, w: tuple) -> np.ndarray:
        """
        """
        n = len(v)
        dp = np.array([-1] * (self._weight + 1), dtype=np.int)
        
        for i in range(n):
            k = 1
            l = self._weight // w[i]
            while k <= l:
                for W in range(self._weight, w[i] * k - 1, -1):
                    if W == w[i] * k:
                        dp[W] = max(dp[W], v[i] * k)
                    elif dp[W - w[i] * k] != -1:
                        dp[W] = max(dp[W - w[i] * k] + v[i] * k, dp[W])
                k *= 2

        return dp

    def wrap_optimum(self, value: tuple, size: tuple) -> np.ndarray:
        """
            : If volumn loop goes from minimum to maximum, then former result(dp[v - size[i]]) has been taken into account
            when checking the volumn of v, and current result(dp[v]) will be checked in the future when the volumn of sack
            reached dp[v + size[i]], this repeats N times where N < (maximum volumn // size[i]). 
            Thus complete knapsack problem is sovled in this way by reversing the loop direction of volumn.
            Note: we do not need to check the volumn of free space even N times i-th item's size is added, because only 
            when v equals N * size[i] + M * size[i - 1] + ... the dp[v - size[i]] equals M * value[i - 1] + ...
        """
        n = len(value)
        dp = np.zeros(self._weight + 1, dtype=np.int)

        for i in range(n):
            for W in range(size[i], self._weight + 1):
                dp[W] = max(dp[W - size[i]] + value[i], dp[W])
        
        return dp

    def wrap_optimum_exact_match(self, value: tuple, size: tuple) -> np.ndarray:
        n = len(value)
        dp = np.array([-1] * (self._weight + 1), dtype=np.int)

        for i in range(n):
            for W in range(size[i], self._weight + 1):
                if W == size[i]:
                    dp[W] = max(value[i], dp[W])
                elif dp[W - size[i]] != -1:
                    dp[W] = max(dp[W - size[i]] + value[i], dp[W])
        
        return dp



knapsack = Knapsack(15)

r1 = knapsack.wrap((12, 3, 10, 3, 6), (5, 4, 7, 2, 6))
print(r1)
r1 = knapsack.wrap_opt((12, 3, 10, 3, 6), (5, 4, 7, 2, 6))
print(r1)

r2 = knapsack.wrap((13, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r2)
r2 = knapsack.wrap_opt((13, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r2)

r3 = knapsack.wrap((12, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r3)
r3 = knapsack.wrap_optimum((12, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r3)

r4 = knapsack.wrap_opt((13, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r4)
r4 = knapsack.wrap_optimum((13, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r4)

r5 = knapsack.wrap_opt((12, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r5)
r5 = knapsack.wrap_optimum((12, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r5)

r6 = knapsack.warp_opt_exact_match((13, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r6)
r6 = knapsack.wrap_optimum_exact_match((13, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r6)

r7 = knapsack.warp_opt_exact_match((12, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r7)
r7 = knapsack.wrap_optimum_exact_match((12, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r7)

pass
