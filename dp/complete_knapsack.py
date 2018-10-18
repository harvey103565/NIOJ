import numpy as np

class Knapsack:
    def __init__(self, volumn: int):
        self._volumn = volumn

    def wrap(self, value: list, cost: list) -> list:
        """
        Wrap all item into knapsack
            : For complete knapsack problem, every item could be taken as many times as it could be. It's ordinary 
            way to treat such item as a set of sigal ones. Then add them into sack one by one. This turns complete 
            knapsack problem into zero one subtype. Since quantity of each items is actually infinite, so we must use 
            volume / cost to determine how many times it could be add. 
            Be noticed that, the dp matrix is extended as items are splitted. However, if we use optimzed method in
            zero one problem, any one demension matrix with the size of v is required. Thus, this is the way.

        """
        n = len(value)
        # TODO: Argument checking
        dp = np.zeros(self._volumn + 1, dtype=np.int)
        
        for i in range(n):
            k = self._volumn // cost[i]
            for l in range(k):
                l = l   # eliminate warning
                for v in range(self._volumn, cost[i] - 1, -1):
                    dp[v] = max(dp[v - cost[i]] + value[i], dp[v])

        return dp

    def wrap_opt(self, value: list, cost: list) -> list:
        """
        Wrap all item into knapsack
            : A small optimization. Items are divided following the rule: [1/2, 1/4, 1/8, ... ] rather than [1, 1, 1]
            So the middle loop(the k-loop) run log(n) times instead of n time.

        """
        n = len(value)
        # TODO: Argument checking
        dp = np.zeros(self._volumn + 1, dtype=np.int)
        
        for i in range(n):
            k = 1
            l = self._volumn // cost[i]
            while k <= l:
                for v in range(self._volumn, cost[i] * k - 1, -1):
                    dp[v] = max(dp[v - cost[i] * k] + value[i] * k, dp[v])
                k *= 2

        return dp

    def warp_opt_exact_match(self, value: list, cost: list) -> list:
        """
        """
        n = len(value)
        # TODO: Argument checking
        dp = np.array([-1] * (self._volumn + 1), dtype=np.int)
        
        for i in range(n):
            k = 1
            l = self._volumn // cost[i]
            while k <= l:
                for v in range(self._volumn, cost[i] * k - 1, -1):
                    if v == cost[i] * k:
                        dp[v] = max(dp[v], value[i] * k)
                    elif dp[v - cost[i] * k] != -1:
                        dp[v] = max(dp[v - cost[i] * k] + value[i] * k, dp[v])
                k *= 2

        return dp

    def wrap_optimum(self, value: list, cost: list) -> list:
        """
            : If volumn loop goes from minimum to maximum, then former result(dp[v - cost[i]]) has been taken into account
            when checking the volumn of v, and current result(dp[v]) will be checked in the future when the volumn of sack
            reached dp[v + cost[i]], this repeats N times where N < (maximum volumn // cost[i]). 
            Thus complete knapsack problem is sovled in this way by reversing the loop direction of volumn.
            Note: we do not need to check the volumn of free space even N times i-th item's cost is added, because only 
            when v equals N * cost[i] + M * cost[i - 1] + ... the dp[v - cost[i]] equals M * value[i - 1] + ...
        """
        n = len(value)
        # TODO: Argument checking
        dp = np.zeros(self._volumn + 1, dtype=np.int)

        for i in range(n):
            for v in range(cost[i], self._volumn + 1):
                dp[v] = max(dp[v - cost[i]] + value[i], dp[v])
        
        return dp

    def wrap_optimum_exact_match(self, value: list, cost: list) -> list:
        n = len(value)
        # TODO: Argument checking
        dp = np.array([-1] * (self._volumn + 1), dtype=np.int)

        for i in range(n):
            for v in range(cost[i], self._volumn + 1):
                if v == cost[i]:
                    dp[v] = max(value[i], dp[v])
                elif dp[v - cost[i]] != -1:
                    dp[v] = max(dp[v - cost[i]] + value[i], dp[v])
        
        return dp



knapsack = Knapsack(14)

r1 = knapsack.wrap((12, 3, 10, 3, 6), (5, 4, 7, 2, 6))
print(r1)

r2 = knapsack.wrap((13, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r2)

r3 = knapsack.wrap_opt((13, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r3)

r4 = knapsack.wrap_optimum((13, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r4)

r5 = knapsack.warp_opt_exact_match((13, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r5)

r6 = knapsack.wrap_optimum_exact_match((13, 3, 10, 5, 6), (5, 4, 7, 2, 6))
print(r6)

pass
